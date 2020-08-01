from django.http import HttpResponseRedirect
from django.urls import reverse
from .helpers import is_logged_in


def logged_in_check(func):

    def inner(request):
        check = is_logged_in(request)
        if not check:
            return HttpResponseRedirect(reverse('admin_login'))
        return func(request)
    return inner