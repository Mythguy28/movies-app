from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies' : ['the house in the woods', 'the ring', 'night of the living dead', 'thir13en ghosts']
    }
    return render(request, 'movies/index.html', context)


def about(request):
    return render(request, 'movies/about.html', {})

# app/templates/app/index.html
# movies/templates/movies/indes.html