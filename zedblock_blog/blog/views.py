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

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            # Create a new post in the database
            new_post = BlogPost(title=title, content=content)
            new_post.save()
            return redirect('home')

    return render(request, 'admin.html', {'error_message': 'Invalid input. Title and content are required.'})

def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # Redirect to the blog list page
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})

def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('postId')

        if post_id.isdigit():
            post_id = int(post_id)
            # Delete the post from the database
            BlogPost.objects.filter(pk=post_id).delete()
            return redirect('home')

    return render(request, 'admin.html', {'error_message': 'Invalid Post ID.'})
