
from . import views
from django.urls import path
from django.conf.urls import url

app_name='localization_app'

urlpatterns =[
    path('', views.index, name='index'),
]