from django.shortcuts import render
from django.http import JsonResponse, Http404
from .settings import MODEL_DIR
from joblib import load
from os import path
from .forms import ClothingFitForm


MODEL = load(path.join(MODEL_DIR, 'model.joblib'))
FEATURE_SCALER = load(path.join(MODEL_DIR, 'scaler.joblib'))
FEATURE_DECOMPOSER = load(path.join(MODEL_DIR, 'decomposer.joblib'))


def index(request):
    if request.method == 'GET':
        form = ClothingFitForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context)

    elif request.method == 'POST':
        return JsonResponse({'sup': 'good'})

    else:
        return Http404()


