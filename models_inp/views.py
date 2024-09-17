from django.shortcuts import render
from . import forms

# Create your views here.


def models_inp(request):
    return render(request, 'models_inp.html',{"form":forms.ModalForm()})