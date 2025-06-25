from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('adc/', views.adc, name='adc'),
    path('equipe/update/<int:pk>/', views.equipe_update, name='equipe_update'),
    path('equipe/delete/<int:pk>/', views.equipe_delete, name='equipe_delete'),
    path('detalhes/<int:pk>/', views.detalhes, name='detalhes'),
    path('registro/', views.registro_publico, name='registro'),
]
