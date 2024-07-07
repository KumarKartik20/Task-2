from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Category
from .forms import BlogPostForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import BlogPostForm
from django.shortcuts import render, redirect
from .forms import BlogPostForm

from django.shortcuts import render, redirect
from .forms import BlogPostForm

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            else:
                post.author = None  # Or handle anonymous user differently if needed
            post.save()
            return redirect('my_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})



def my_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})

def list_posts(request):
    categories = Category.objects.all()
    posts = {category: BlogPost.objects.filter(category=category, is_draft=False) for category in categories}
    return render(request, 'blog/list_posts.html', {'posts': posts, 'categories': categories})
