from django.urls import path
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("search/<str:query>", views.search, name="search")
]
