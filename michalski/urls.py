"""michalski URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import MyViewMain, MyViewContact, MyViewStart, MyViewRent, MyViewGlowna, MyViewLoan, MyViewTax, MyViewInsurance, MyViewSzkoda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('glowna_fin', MyViewMain.as_view(), name = 'glowna_fin.html'),
    path('', MyViewStart.as_view(), name = 'start.html'),
    path('contact', MyViewContact.as_view(), name = 'contact.html'),
    path('rent', MyViewRent.as_view(), name = 'rent.html'),
    path('glowna_pomoc', MyViewGlowna.as_view(), name = 'glowna_pomoc.html'),
    path('loan', MyViewLoan.as_view(), name = 'loan.html'),
    path('tax', MyViewTax.as_view(), name = 'tax.html'),
    path('insurance', MyViewInsurance.as_view(), name = 'insurance.html'),
    path('szkoda',MyViewSzkoda.as_view(), name = 'szkoda.html')
    
    ]