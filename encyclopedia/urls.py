from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("css", views.css, name="css"),
    path("Django", views.django, name="django"),
    path("Git", views.git, name="git"),
    path("HTML", views.html, name="html"),
    path("Python", views.py, name="python")
]
