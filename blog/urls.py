from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name = "landing-page"),
    path("posts", views.posts),
    path("post/<slug>", views.article)
]
