from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegForm


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
