from django.urls import path
from formulario.views import index

urlpatterns = [
    path('', index),
]