from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cats index
    path('pedals/', views.pedals_index, name='index'),
]
