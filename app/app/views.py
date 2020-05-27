from django.shortcuts import render
from django.http import JsonResponse, Http404
from .settings import MODEL_DIR
from joblib import load
from os import path
from .forms import ClothingFitForm
from .utils import get_feature_vector, calc_bmi, normalize_to_range
import numpy as np


MODEL = load(path.join(MODEL_DIR, 'model.joblib'))
FEATURE_SCALER = load(path.join(MODEL_DIR, 'scaler.joblib'))
VAR_THRESHOLDER = load(path.join(MODEL_DIR, 'bool_var_th.joblib'))


def index(request):
    if request.method == 'GET':
        form = ClothingFitForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context)

    elif request.method == 'POST':
        form = ClothingFitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prod_cat = get_feature_vector(data['product_category'],
                                          path.join(MODEL_DIR, 'txt/product_categories.txt'))
            prod_size = normalize_to_range(
                get_feature_vector(data['product_size'],
                                   path.join(MODEL_DIR, 'txt/size_categories.txt'),
                                   True),
                min_allowed=0.0, max_allowed=58.0,
                min=1.0, max=8.0)

            rented_for = get_feature_vector(data['rented_for'],
                                            path.join(MODEL_DIR, 'txt/rented_for_categories.txt'))

            body_type = get_feature_vector(data['body_type'],
                                           path.join(MODEL_DIR, 'txt/body_type_categories.txt'))

            age = data['age']
            bmi = calc_bmi(data['weight'], data['height'])

            boolead_features = np.hstack((prod_cat, rented_for, body_type))
            boolead_features = VAR_THRESHOLDER.transform(boolead_features.reshape(1, -1))

            features = np.hstack((prod_size, age, bmi,
                                  boolead_features.squeeze())).reshape(1, -1)
            features = FEATURE_SCALER.transform(features)

            prediction = MODEL.predict(features)[0]

            if prediction == 1:
                pred_response = 'This clothing should be large for you!'
            elif prediction == -1:
                pred_response = 'This closing should be small for you!'
            else:
                pred_response = 'This should be the right one!'

            context = {
                'form': form,
                'prediction': pred_response
            }
        else:
            context = {
                'form': form
            }

        return render(request, 'index.html', context)

    else:
        return Http404()


