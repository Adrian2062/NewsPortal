from django.urls import path
from .views import HomeView
from . import views
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
]
