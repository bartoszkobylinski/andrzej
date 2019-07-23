from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class InsuranceForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    surname = forms.CharField(label='surname', max_length=100)
    phone = PhoneNumberField()
    email = forms.EmailField()

class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    surname = forms.CharField(label='surname', max_length=100)
    phone = forms.DecimalField(label='phone', max_digits=31)
    email = forms.EmailField()
    subject = forms.CharField(label='subject', max_length=100)
    comment = forms.CharField(label = 'comment', widget = forms.Textarea)
    '''
    class Meta:
        fields=('name','surname','phone','email','subject','comment')
'''