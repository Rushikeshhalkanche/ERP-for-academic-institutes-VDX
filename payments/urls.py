from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_payment, name='add_payment'),
    path('success/', views.success_view, name='success'),  # This resolves the error
]
