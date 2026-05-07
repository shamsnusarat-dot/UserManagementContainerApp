from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, user)
            return redirect('user-list-template')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
