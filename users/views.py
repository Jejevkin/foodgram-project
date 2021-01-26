from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from users.forms import CreationForm


def signup_view(request):
    form = CreationForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'signup.html', context)
