from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:id>/', views.delete_item, name='delete'),
    path('count/', views.required_view, name='required'),
]
