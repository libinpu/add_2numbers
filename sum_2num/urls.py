# myapp/urls.py
from django.urls import path
from .views import add_numbers, get_all_data

urlpatterns = [
    path('add/', add_numbers, name='add_numbers'),
    path('get-all/', get_all_data, name='get_all_data'),
]
