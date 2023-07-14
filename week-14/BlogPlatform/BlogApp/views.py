from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Author

def home(request):
    return render(request, "home.html")

def view_post(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "post.html", context)

def view_post_detail(request,id):
    post = get_object_or_404(Post, pk=id)
    context = {"post": post}
    return render(request, "post_details.html", context)

def view_category(request):
    categories = Category.objects.all()
    context = {"categories" : categories }
    return render(request, "category.html", context)

def view_category_detail(request,id):
    category = get_object_or_404(Category, pk=id)
    context = {"category": category}
    return render(request, "category_details.html", context)

def view_authors(request):
    authors = Author.objects.all()
    context = {"authors" : authors }
    return render(request, "author.html", context)