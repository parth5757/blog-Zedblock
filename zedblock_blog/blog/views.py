from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
# from blog.models import BlogPost


def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def admin(request):
    posts = BlogPost.objects.all()
    return render(request, 'admin.html', {'posts': posts})

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'edit_post.html', {'posts': post})

def add_edit_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('postId')
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            if post_id:
                # Editing an existing post
                post = get_object_or_404(BlogPost, pk=post_id)
                post.title = title
                post.content = content
                post.save()
            else:
                # Adding a new post
                BlogPost.objects.create(title=title, content=content)

            return redirect('admin')

    return render(request, 'admin.html', {'posts': BlogPost.objects.all(), 'error_message': 'Invalid input. Title and content are required.'})

def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    return redirect('admin')