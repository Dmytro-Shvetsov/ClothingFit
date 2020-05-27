from django import forms
from os import path
from .settings import MODEL_DIR
from .utils import get_choices


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

    age = forms.IntegerField(
        label='Your age',
        min_value=14,
        widget=forms.NumberInput({
            'class': 'form-input',
            'placeholder': 'Age'})
    )
    weight = forms.FloatField(
        label='Your weight in kilograms',
        min_value=30.0,
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

    body_type = forms.ChoiceField(
        label='Your body type',
        choices=get_choices(path.join(MODEL_DIR, 'txt/body_type_categories.txt')),
        widget=forms.Select({'class': 'form-input'})
    )

    class Meta:
        fields = ('product_category', 'product_size', 'rented_for',
                  'age', 'weight', 'height', 'body_type')
