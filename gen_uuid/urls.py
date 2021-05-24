from django.urls import path
from . import views

urlpatterns = [
    path('', views.gen_uuid, name='gen_uuid'),
]