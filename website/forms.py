from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class InsuranceForm(forms.Form):
    name = forms.CharField(label = 'name', max_length=100)
    surname = forms.CharField(label = 'surname', max_length=100)
    phone = PhoneNumberField()
    email = forms.EmailField(label = 'email', required = False)

class ContactForm(forms.Form):
    name = forms.CharField(label = 'name', max_length=100)
    surname = forms.CharField(label = 'surname', max_length=100)
    phone = PhoneNumberField()
    email = forms.EmailField(label = 'email', required = True)
    comment = forms.CharField(label = 'comment', widget = forms.Textarea)
