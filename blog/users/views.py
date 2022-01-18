from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegForm
from app.models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = RegForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def post(request,post):
    if request.user.is_authenticated:#useless check, just for debugging
        posts=Post.objects.filter(author_id=request.user.id, pk=post).exists()#check if post there
        if posts:
            #posts=get_object_or_404(post_check, pk=post) for post doesnt exist
            posts=Post.objects.get(author_id=request.user.id, pk=post)
            context = {
                'posts':posts,
                'title':'Post',
                'date':timezone.now
            }
            return render(request, 'users/post.html',context)
        else:
            return redirect('home')

    else:
        return redirect('home')

@login_required #login required to acces this function,
def update(request):
        if request.method == "POST":
            title=request.POST['title']
            author_id=request.POST['user_id']#if user id needed, for author
            content=request.POST['content']
            post_id=request.POST['post_id']
            date=timezone.now() #current time
            post_check=Post.objects.all().filter(author_id=author_id)
            if post_check:#no use
            #if request.user.is_authenticated:
                post_update=Post(id=post_id,title=title, author_id=author_id, content=content, date=date)
                post_update.save()
                messages.success(request,'Post updated !')

                return redirect('home')
            else:
                return redirect('home')
        else:
            return redirect('home')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm() #instence
#         if form.is_valid():# all fields valid
#             form.save()
#             username = form.cleaned_data.get('username') #foram data will be in cleaned_data dictionary,
#             messages.success(request, f"account created for {username}")
#             return redirect('home')
#     else:
#         form = UserCreationForm() #Empty form
#         return render(request,'users/register.html',{'form':form})
