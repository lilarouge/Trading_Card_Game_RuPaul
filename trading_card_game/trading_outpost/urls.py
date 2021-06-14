from django.urls import path
from . import views

urlpatterns = [
    # path('homepage/', views.get_queens, name='homepage'),
    path('allqueens/', views.get_queens, name='get_queens'),
    path('transaction/', views.my_exchange, name='transaction'),
    path('my_offers/', views.my_offers, name='my_offers'),
    
]