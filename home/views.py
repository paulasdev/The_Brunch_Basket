from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def not_found_404(request, exception):
    """ A view to return the 404 page """

    return render(request, 'home/404.html')


