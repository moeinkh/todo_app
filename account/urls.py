from django.urls import path
from .views import sign_up, profile

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('signup/', sign_up, name='sign_up'),
]