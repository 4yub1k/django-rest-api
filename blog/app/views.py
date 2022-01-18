from django.shortcuts import render
from .models import Post
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