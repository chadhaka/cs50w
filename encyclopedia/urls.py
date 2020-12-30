from django.urls import path
from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name="newpage"),
    path("random", views.random, name="random"),
    path("<str:entry>", views.entry, name="entry"),
    path("search/<str:query>", views.search, name="search"),
    path("search", views.search, name="search"),
    path("edit/<str:entry>", views.edit, name="edit")
    
]
