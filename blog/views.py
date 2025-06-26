from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return HttpResponse("<h1>Welcome to the CSE Blog</h1>")

def post_list(request):
    posts = Post.objects.all()
    html = "<h1>Blog Posts</h1>"
    for post in posts:
        html += f"<h2>{post.title}</h2><p>{post.content}</p><hr>"

    return HttpResponse(html)

def post_details(request, post_id):
    post = Post.objects.get(id = post_id)
    html = f"<h1>{post.title}</h1><p>{post.content}</p><p>Created at: {post.created_at}</p>"
    return HttpResponse(html)
