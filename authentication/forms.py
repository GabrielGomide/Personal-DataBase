from django import forms

class CreateAccountForm(forms.Form):
    password = forms.CharField(label="", max_length=100, 
    widget=forms.PasswordInput(attrs={'placeholder': 'Password:'}))


