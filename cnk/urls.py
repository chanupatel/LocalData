from django.urls import path
from polls import views
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
