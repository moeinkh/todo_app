from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.delete_task, name='delete_task'),
]