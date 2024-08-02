from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("random_page", views.random_page, name="random_page"),
    path("wiki/<str:name>", views.unkown, name="unkown")
]
