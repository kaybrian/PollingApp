from django.urls import path 
from . import views

app_name='polls'

urlpatterns = [
    path('',views.index,name='index'),
    path('results/',views.result,name='result'),
    path('vote/',views.vote,name='vote'),
    path('create',views.Create,name='create'),
]
