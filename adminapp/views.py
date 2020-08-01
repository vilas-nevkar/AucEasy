from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from util.decorators import logged_in_check
from .forms import UserRegisterForm, UserLoginForm
from .models import AdminUser


@logged_in_check
def dashborad(request):
    return render(request, 'dashboard.html', {'section': 'Dashborad'})


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(data=request.POST)
        print(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            user_form.save()
            return render(request, 'registration/registration_done.html', {})
        else:
            user_form = UserRegisterForm()
            return render(request, 'registration/register.html', {'user_form': user_form})

    else:
        user_form = UserRegisterForm()
        return render(request, 'registration/register.html', {'user_form': user_form})


def user_login(request):
    """
    User login view
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # manually getting User object
            user = AdminUser.objects.get(
                admin_username=cd['username'],
                admin_email=cd['email'],
                admin_password=cd['password']
            )

            if user:
                user_data = {'username': cd['username'], 'email': cd['email']}
                session = request.session
                session['user_data'] = user_data
                return HttpResponseRedirect(reverse('dashboard'))

            else:
                return HttpResponse('Invalid Login')
        else:
            print(form.errors)
            form = UserLoginForm()
            return render(request, 'registration/login.html', {'form': form})

    else:
        form = UserLoginForm()
        return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    session = request.session
    session.flush()
    return HttpResponse("logout")
