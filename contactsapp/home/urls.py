from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<id>', views.contact, name='contact'),
    path('addnew/', views.addnew, name='addnew'),
    path('edit/', views.editexisting, name='edit'),
    path('edit/<id>', views.editContact, name='edit-contact'),
    path('delete/', views.delete, name='delete'),
    path('delete/deletecontact', views.deletecontact, name='deletecontact'),
]
