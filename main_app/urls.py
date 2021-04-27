from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pedals/', views.pedals_index, name='index'),
    path('pedals/<int:pedal_id>', views.pedals_detail, name='details'),
    path('pedals/create/', views.PedalCreate.as_view(), name='pedals_create'),
    path('pedals/<int:pk>/update/', views.PedalUpdate.as_view(), name='pedals_update'),
    path('pedals/<int:pk>/delete/', views.PedalDelete.as_view(), name='pedals_delete'),
    path('pedals/<int:pedal_id>/add_show/', views.add_show, name='add_show'),
    path('pedals/<int:pedal_id>/assoc_instrument/<int:instrument_id>/', views.assoc_instrument, name='assoc_instrument'),


    # instrument urls
    path('instruments/', views.instruments_index, name='all_instruments'),
    path('instruments/<int:instrument_id>/', views.instrument_detail, name='instrument_detail'),
    path('instruments/create/', views.Create_instrument.as_view(), name='create_instrument'),
    path('instruments/<int:pk>/update/', views.Update_instrument.as_view(), name='update_instrument'),
    path('instruments/<int:pk>/delete/', views.Delete_instrument.as_view(), name='delete_instrument'),
    path('pedals/<int:pedal_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]
