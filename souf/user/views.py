from django.shortcuts import render
from .models import User
from .forms import UserForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
    render(request, 'index.html')
