from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from usuarios.models import Usuario
from .models import Review

# Create your views here.

TMDB_API_KEY = "e3c8832537a6cdad4f0a8f3f9b160e2f"

def index(request):
    data = requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate')
    if request.session.get('usuario'):
        return render(request, 'home.html', {
            "data": data.json(),
            "usuario_logado": request.session.get('usuario')
        })
    else:
        return redirect('/auth/login/')

def search(request):
    query = request.GET.get('search')
    print(query)
    if query:
        data = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&page=1&query={query}')
        print(data)
        return render(request, 'search.html', {
            "data": data.json(),
            "usuario_logado": request.session.get('usuario')
        })
    else:
        return redirect('/')

def ver_detalhes(request, movie_id):
    data = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US')

    return render(request, 'ver_detalhes.html', {
        "data": data.json(),
        "usuario_logado": request.session.get('usuario'),
        "user": Usuario.id
    })

def avaliar(request):
    user = Usuario.id
    id_filme = request.GET.get('data.id')
    opcoes = request.GET.get('opcoes')

    avaliacao = Review(user=user, filme=id_filme, rate=opcoes)
    
    return HttpResponse('foi')