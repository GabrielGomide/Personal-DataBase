from django import forms
import datetime

# Create your models here.
class AddPeople(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Name'}), label='')
    birthday = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Birthday'}), label='', required=False)
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'E-mail'}), label='', required=False)
    number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}), label='', required=False)
    instagram = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Instagram'}), label='', required=False)
    notes = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Notes'}), label='', required=False)

class AddNote(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Title'}), label='')
    notes = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'placeholder': 'Notes'}), label='')
