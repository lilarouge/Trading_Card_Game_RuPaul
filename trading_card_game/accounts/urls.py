from django.urls import path, include
from . import views
from trading_outpost import views as accept_offer_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', accept_offer_views.accept_offer, name='profile'),
    path('my_cards/', views.my_cards, name='my_cards'),
]