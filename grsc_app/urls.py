from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home.html', TemplateView.as_view(template_name='home.html'), name='home'),
    path('donate.html', TemplateView.as_view(template_name='donate.html'), name='donate'),
    path('students.html', TemplateView.as_view(template_name='students.html'), name='students'),
]

