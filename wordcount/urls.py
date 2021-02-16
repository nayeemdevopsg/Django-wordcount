
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('counttheworld/', views.count,  name='count'),
    path('aboutpage/', views.about, name='about'),
    
]
