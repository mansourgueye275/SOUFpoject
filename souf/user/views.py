from django.shortcuts import render, redirect,reverse
from django.db import IntegrityError
from .models import User
from .forms import UserForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                telephone=form.cleaned_data['telephone'])

            # ensure encrypted password
            user.set_password(form.cleaned_data['password'])
            try:
                user.save()
                return redirect(reverse(viewname='home'))
            except IntegrityError:
                form.add_error(user.email+" is already used to register")
            else:
                pass

    else:
        form= UserForm()
    return render(request, 'signup.html',{'form': form})
