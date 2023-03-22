from django.contrib import admin
from django.urls import path, include
from basicConcepts import views

urlpatterns = [
    path('',include('basicConcepts.urls')),
    path('admin/', admin.site.urls)
]
