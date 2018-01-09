from django.shortcuts import render, redirect,reverse
from django.db import IntegrityError
from .models import User
from .forms import UserForm, SigninForm

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
                return redirect(reverse(signup(request)))
            else:
                pass

    else:
        form= UserForm()
    return render(request, 'signup.html',{'form': form})



def signin(request):
    user = None
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            results = User.objects.filter(email=form.cleaned_data['email'])
            if len(results) == 1:
                if results[0].check_password(form.cleaned_data['password']):
                    request.session['user'] = results[0].pk
                    return redirect('/')
                else:
                    form.add_error('__all__','mot de passe incorrect')
            else:
                form.add_error('__all__','adresse email incorrect')
    else:
        form = SigninForm()

    print(form.non_field_errors())

    return render(
        request,
        'signin.html',
        {
            'form': form,
            'user': user
        }
    )


def signout(request):
    del request.session['user']
    return redirect('/')




