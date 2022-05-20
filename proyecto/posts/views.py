from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'home.html')


def posts(request):
    posts = Post.objects.all().order_by("-created_date", "-id")   # SELECT * FROM posts

    
    print(posts)
    # return HttpResponse("Publicaciones")

    return render(request, 'posts/posts.html', {
        'posts': posts
    })

def search(request):

    if request.method == "POST":
        posts = Post.objects.filter(title__icontains=request.POST["busqueda"]).order_by("-created_date", "-id") # SELECT * FROM posts WHERE title LIKE "Publicación"

    return render(request, 'posts/posts.html', {
        'posts': posts
    })
 

def post(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'posts/post.html', {'post':post})


def create_post(request):
    if request.method == "POST":
        post = Post(
            title=request.POST['title'],
            category=request.POST['category'],
            description=request.POST['description'],
            img=request.POST['image'],
            content=request.POST['content'],
            author=request.user
        )

        post.save()

        return redirect("/posts")

    return render(request, 'posts/create.html')


def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":

        post.title = request.POST['title']
        post.description = request.POST['description']
        post.img = request.POST['image']
        post.content = request.POST['content']


        post.save()

        return redirect("/posts")

    return render(request, 'posts/edit.html', {'post': post})


def delete_post(request,id):
    post = Post.objects.get(id=id)

    post.delete()
    return redirect("/posts")