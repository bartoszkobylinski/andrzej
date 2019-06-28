from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import InsuranceForm, ContactForm
from django.core.mail import send_mail

# Create your views here.

class MyViewMain(View):
    def get(self,request):
        return render(request, 'glowna_fin.html')

class MyViewStart(View):
    def get(self,request):
        return render(request, 'start.html')

class MyViewContact(View):
    def get(self,request):
        return render(request,'contact.html')
    def post(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = 'Formularz kontaktowy ze strony www.pomocdrogowa.pisz.pl nr'
                text = 'ktos wlasnie wyslal do Ciebie formularz z zapytaniem o uslugi finansowe'
                email_sender = 'bartosz.kobylinski@gmail.com'
                email_reciver = ['bartosz.kobylinski@gmail.com']
                send_mail(subject,
                text,
                email_sender,
                email_reciver,
                fail_silently=False,
                )
                return HttpResponseRedirect('glowna_pomoc')
        else:
            form = InsuranceForm()

        return render(request, 'insurance.html', { 'form': form })

class MyViewRent(View):
    def get(self,request):
        return render(request, 'rent.html')

class MyViewGlowna(View):
    def get(self,request):
        return render(request, 'glowna_pomoc.html')

class MyViewLoan(View):
    def get(self,request):
        return render(request, 'loan.html')

class MyViewTax(View):
    def get(self, request):
        return render(request, 'tax.html')

class MyViewInsurance(View):
    
    def post(self, request):
        if request.method == 'POST':
            form = InsuranceForm(request.POST)
            if form.is_valid():
                subject = 'Formularz kontaktowy ze strony www.pomocdrogowa.pisz.pl nr'
                text = 'ktos wlasnie wyslal do Ciebie formularz z zapytaniem o uslugi finansowe'
                email_sender = 'bartosz.kobylinski@gmail.com'
                email_reciver = ['bartosz.kobylinski@gmail.com']
                send_mail(subject,
                text,
                email_sender,
                email_reciver,
                fail_silently=False,
                )
                return HttpResponseRedirect('glowna_pomoc')
        else:
            form = InsuranceForm()

        return render(request, 'insurance.html', { 'form': form })

    def get(self, request):
        return render(request, 'insurance.html')
        
class MyViewSzkoda(View):
    def get(self, request):
        return render(request, 'szkoda.html')

