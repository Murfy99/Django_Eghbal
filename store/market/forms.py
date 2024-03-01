from typing import Any
from django import forms 
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import *
import re

PHONE_REGEX = re.compile(r'^(\+98|0|0098)?9\d{9}$')

class ContactUsForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    age = forms.IntegerField(validators=[
        MaxValueValidator(100,'age must be less than 100'),
        MinValueValidator(18,'age must be above 18'),
    ])
    msg = forms.CharField(widget=forms.Textarea)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone').strip()
        if not PHONE_REGEX.search(phone):
            raise ValidationError("invalid phone number")
        return phone



    def clean(self) -> dict[str, Any]:
        r = super(ContactUsForm,self).clean()
        if not self.cleaned_data.get('phone') and not self.cleaned_data.get('email'):
            raise ValidationError('at least one required')
        return r
    
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
