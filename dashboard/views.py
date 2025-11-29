# dashboard/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm

# List all posts
class AdminDashboardView(ListView):
    model = Post
    template_name = "dashboard/post_list.html"
    context_object_name = "posts"

# Create a new post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PostForm()
    return render(request, 'dashboard/post_form.html', {'form': form, 'title': 'Add Post'})

# Update post
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PostForm(instance=post)
    return render(request, 'dashboard/post_form.html', {'form': form, 'title': 'Edit Post'})

# Delete post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('admin_dashboard')
    return render(request, 'dashboard/post_confirm_delete.html', {'post': post})
