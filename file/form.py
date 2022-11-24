from django import forms

class Form(forms.Form):
    docfile = forms.FileField(label="Selecione um arquivo")