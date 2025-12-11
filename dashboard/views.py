from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm

# List all posts
class AdminPostListView(ListView):
    model = Post
    template_name = "dashboard/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')  # FIXED

# Create a new post
class AdminPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "dashboard/post_create.html"
    success_url = reverse_lazy('dashboard:post-list')

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')  # FIXED

class AdminPostDeleteView(View):

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('dashboard:post-list')
