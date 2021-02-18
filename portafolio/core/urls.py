from django.urls import path
from .views import HomePageView, AboutPageView, contacto

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contacto, name='contact'),
]