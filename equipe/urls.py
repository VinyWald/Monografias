from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('list',views.list,name='lista'),
    path('adicionar',views.adc,name='adicionar'),
    path('update/<int:pk>/', views.equipe_update, name='equipe_update'),
    path('delete/<int:pk>/', views.equipe_delete, name='equipe_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)