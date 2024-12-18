from django.urls import path
from . import views

urlpatterns = [
    path("january",views.Jan),
    path("febuary",views.Feb)
]
