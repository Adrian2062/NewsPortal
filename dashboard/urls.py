# dashboard/urls.py
from django.urls import path
from .views import AdminDashboardView, post_create, post_update, post_delete

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('create/', post_create, name='post-create'),
    path('<int:pk>/update/', post_update, name='post-update'),
    path('<int:pk>/delete/', post_delete, name='post-delete'),
]
