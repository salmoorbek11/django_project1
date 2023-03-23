from django.urls import path

from pages.views import home_page, about, contacts, create

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('create/', create)
]