from django.urls import path
from . import views

urlpatterns = [
    path('', views.kitob, name='kitob'),
    path('buy/<str:kitob_nomi>/', views.sotib_olish, name='sotib_olish'),
]