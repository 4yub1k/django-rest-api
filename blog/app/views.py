from .models import Post
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#list-dictionary
# posts = [
#         {
#             'author':'Ayubi',
#             'title':'New post',
#             'content':'New technology',
#             'date':'1/1/9000'
#         },
#         {
#             'author':'Ayubi',
#             'title':'New post',
#             'content':'New technology',
#             'date':'1/1/9000'
#         }
#         ]

def home(request):
    posts=Post.objects.all()
    context = {
        'posts':posts,
        'title':'Home'
    }
    return render(request,'app/home.html',context)
def about(request):
    return render(request,'app/about.html',{'title':'About'})
    
def post_(request, post):
    posts=Post.objects.filter(pk=post).exists()#check if post there
    if posts:
        #posts=get_object_or_404(post_check, pk=post) for post doesnt exist
        posts=Post.objects.get(pk=post)
        context = {
            'posts':posts,
            'title':'Post',
        }
        return render(request,'users/post_.html',context)
    else:
        return redirect('home')

@login_required
def add(request):
    if request.method == "POST":
        title=request.POST['title']
        content=request.POST['content']
        #post_check=Post.objects.all().filter(author_id=author_id)
        post_add=Post(author_id=request.user.id,title=title,content=content)
        post_add.save()
        messages.success(request,'Post Added !')
        return redirect('home')
    return render(request, 'users/addpost.html',{'title':'Post','date':timezone.now})