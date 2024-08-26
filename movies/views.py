from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie

# Create your views here.
def index(request):
    movies=Movie.objects.all()
    return render(request, 'index.html',{'movies':movies})
    #output =','.join([m.title for m in movies])
    #Movie.objects.filter(release_year=1984) #filter
    #Movie.objects.get(id=1)
    #return HttpResponse(output)

def detail(request, movie_id):
    movie=get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html',{'movie':movie})
    