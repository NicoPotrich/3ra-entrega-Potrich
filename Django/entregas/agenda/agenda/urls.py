from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('task/', include('task.urls')),
    path('meetings/', include('meetings.urls')),
    path('', views.index, name='index')
]
