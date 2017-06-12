from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)