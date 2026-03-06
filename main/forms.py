"""all django forms here"""
from django import forms

"""Student login form"""
class StudentLoginForm(forms.Form):
    userName = forms.CharField(
        max_length=50,
        label="Username",
        widget=forms.TextInput(attrs={
            "class": "field-input",
            "placeholder": "Your student username"
        })
    )

    stuPwd = forms.CharField(
        max_length=100,
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "field-input",
            "placeholder": "••••••••"
        })
    )
    