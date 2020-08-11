from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from util.decorators import logged_in_check
from django.core.paginator import Paginator

from .forms import UserRegisterForm, UserLoginForm, ProductFilterForm
from .models import AdminUser
from productapp.models import ProductInformation


@logged_in_check
def dashborad(request):
    user_data = request.session.get('user_data', None)
    print(user_data)
    return render(request, 'dashboard.html', {'section': 'Dashborad', 'user_data': user_data})


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(data=request.POST)
        # user_form.save()
        print(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            user_form.save()
            return render(request, 'registration/registration_done.html', {})
        else:
            user_form = UserRegisterForm()
            return redirect(request, 'registration/register.html', {'user_form': user_form})

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
                # return HttpResponseRedirect(reverse('dashboard'))
                return render(request, 'dashboard.html', {'section': 'Dashborad', 'username': user_data['username']})
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


def view_products(request):
    products = ProductInformation.objects.filter(product_verify=False)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = ProductFilterForm(data=request.GET)
    if form.is_valid():
        print(form.cleaned_data)

    else:
        print(form.errors)
    return render(request, 'view-products.html', {'count': products.count(), 'page_obj': page_obj, 'filters': form})


def verify_products(request, product_id=None):
    # for one product only
    if product_id:
        # get the product
        product = ProductInformation.objects.get(productinformation_id=product_id)
        # update value
        product.product_verify = True
        # save
        product.save()
        return HttpResponseRedirect(reverse('view_products'))


def view_verified_products(request):
    products = ProductInformation.objects.filter(product_verify=True)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'verified-products.html', {'count': products.count(), 'page_obj': page_obj})
