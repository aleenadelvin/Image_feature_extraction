from django.urls import path
from . import views

urlpatterns = [
    path('',views.Welcome, name='welcome'),
    path('upload-image/', views.upload_image, name='forminfo')
    
]