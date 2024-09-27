from django.shortcuts import redirect
from django.urls import reverse


def root_redirect(request):
    language = request.LANGUAGE_CODE
    return redirect(reverse('shopapp:index', args=[language]))
