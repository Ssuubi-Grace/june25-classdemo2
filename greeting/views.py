"""Views for the greeting app."""

from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    """Render the index page with a greeting."""

    return render(request, 'index.html', {'greeting': 'Hello'})
