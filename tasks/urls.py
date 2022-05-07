from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update/<int:id>/', views.active_task, name='active_task'),
]