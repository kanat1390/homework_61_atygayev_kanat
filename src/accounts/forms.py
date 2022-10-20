from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=50, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput())
    



