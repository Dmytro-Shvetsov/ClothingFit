from django import forms
from os import path
from .settings import MODEL_DIR


def get_choices(fp):
    with open(fp) as fid:
        choices = map(lambda x: x.strip(), fid.readline().split(','))
        return tuple([(item.lower(), item) for item in choices])


class ClothingFitForm(forms.Form):
    product_category = forms.ChoiceField(
        label='Category of your product',
        choices=get_choices(path.join(MODEL_DIR, 'txt/product_categories.txt')),
        widget=forms.Select({'class': 'form-input'})
    )
    product_size = forms.ChoiceField(
        label='Size of your product',
        choices=get_choices(path.join(MODEL_DIR, 'txt/size_categories.txt')),
        widget=forms.Select({'class': 'form-input'})
    )
    rented_for = forms.ChoiceField(
        label='Purpose of renting the product',
        choices=get_choices(path.join(MODEL_DIR, 'txt/rented_for_categories.txt')),
        widget=forms.Select({'class': 'form-input'})
    )
    review_rating = forms.FloatField(
        label='Your rating to the product(1-5)',
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(
            {'class': 'form-input',
             'placeholder': 'Rating'})
    )
    age = forms.IntegerField(
        label='Your age',
        min_value=1,
        widget=forms.NumberInput({
            'class': 'form-input',
            'placeholder': 'Age'})
    )
    weight = forms.FloatField(
        label='Your weight in kilograms',
        min_value=1.0,
        widget=forms.NumberInput({
            'class': 'form-input',
            'placeholder': 'Weight'})
    )
    height = forms.FloatField(
        label='Your height in meters',
        min_value=1.0,
        widget=forms.NumberInput({
            'class': 'form-input',
            'placeholder': 'Height'})
    )

    bust_size_num = forms.IntegerField(
        label='Your bust size',
        min_value=1,
        widget=forms.NumberInput({
            'class': 'form-input',
            'placeholder': 'Bust size'})
    )
    bust_size_cat = forms.ChoiceField(
        choices=get_choices(path.join(MODEL_DIR, 'txt/bust_size_categories.txt')),
        widget=forms.Select({'class': 'form-input'})
    )
    body_type = forms.ChoiceField(
        label='Your body type',
        choices=get_choices(path.join(MODEL_DIR, 'txt/body_type_categories.txt')),
        widget=forms.Select({'class': 'form-input'})
    )

    class Meta:
        fields = ('product_category', 'product_size', 'rented_for',
                  'review_rating', 'age', 'weight', 'height',
                  'bust_size_num', 'bust_size_cat', 'body_type')
