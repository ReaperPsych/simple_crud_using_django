from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
