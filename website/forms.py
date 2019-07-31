from django import forms
from website.models import ContactScheme, Post
from phonenumber_field.modelfields import PhoneNumberField

class InsuranceForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    surname = forms.CharField(label='surname', max_length=100)
    phone = PhoneNumberField()
    email = forms.EmailField()

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    subject = forms.CharField(label='subject', max_length=100)
    comment = forms.CharField(label = 'comment', widget = forms.Textarea)
    
    class Meta:
        model = ContactScheme
        fields=('name','email','subject','comment',)

class PostForm(forms.ModelForm):
    text = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = ('text',)