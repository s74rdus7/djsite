from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import *

class AddPlaceForm(forms.ModelForm):
    class Meta:
        model = PLACES
        fields = ['username',
                  'gmail',
                  'password1',
                  'password2',
                  'PLACE_NAME',
                  'PLACE_ADRES',
                  'PLACE_PHOTO',
                  'FIO_DIR',
                  'PLACE_CONTACT_NUMBER',
                  'DOCUMENTS_DLYA_PRIEMA',
                  'slug']
    captcha = CaptchaField()


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['FIRST_NAME',
                  'LAST_NAME',
                  'IIN',
                  'PHOTO_3x4',
                  'WORK_PLACE',
                  'JOB_TITLE',
                  'Svyaz',
                  'slug']
    captcha = CaptchaField()

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['EVENT_NAME',
                  'EVENT_CREATER',
                  'PROTOCOL',
                  'DATE_START',
                  'DATE_END',
                  'PHOTO_FROM_EVENT',
                  'Svyaz',
                  'slug']
    captcha = CaptchaField()