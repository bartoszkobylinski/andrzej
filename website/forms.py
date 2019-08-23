from django import forms
from website.models import ContactScheme, Post

class InsuranceForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    surname = forms.CharField(label='surname', max_length=100)
    email = forms.EmailField()

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='imię i nazwisko', max_length=100)
    email = forms.EmailField(label='email', error_messages={'invalid':'adres e-mail musi posiadac znak @'})
    subject = forms.CharField(label='temat', max_length=100,)
    comment = forms.CharField(label = 'wiadomość', widget = forms.Textarea(attrs={'class':'comment'}))
    
    class Meta:
        model = ContactScheme
        fields=('name','email','subject','comment',)

class PostForm(forms.ModelForm):
    text = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = ('text',)