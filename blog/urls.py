from django.urls import path

urlpatterns = [
    path("", views.starting_page),
    path("posts", views.posts),
    path("post/<slug>", views.article)
]
