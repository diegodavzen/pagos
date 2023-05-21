"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from payment.views import validate_credit_card, previous_view
from django.views.generic import TemplateView

urlpatterns = [

    path('', previous_view, name='previous'),
    path('payment/', TemplateView.as_view(template_name='payment.html'), name='payment'),
    path('validate/', validate_credit_card, name='validate_credit_card'),
    # path('validate/', validate_credit_card, name='validate_credit_card'),
    # #Poner direciones
    # path('payment/', TemplateView.as_view(template_name='payment/payment.html'), name='payment'),
]