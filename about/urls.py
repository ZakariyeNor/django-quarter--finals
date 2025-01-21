from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.about_me, name='about'),
]
