# dashboard/urls.py
from django.urls import path
from .views import AdminPostListView, AdminPostCreateView
from dashboard import views
app_name = 'dashboard'

urlpatterns = [
    path('', AdminPostListView.as_view(), name='admin_dashboard'),
    path("post-create/", AdminPostCreateView.as_view(), name="post_create"),
    path("post-delete/<int:pk>/", views.AdminPostDeleteView.as_view(), name="post_delete"),
]
