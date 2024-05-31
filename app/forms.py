from django import forms

class Uploadfile(forms.Form):
    file = forms.FileField(label='File')

