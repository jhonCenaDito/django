from django.http import HttpResponse
from django.template import loader
from app.models import Player, Post

def index(request):
    template = loader.get_template('index.html')
    context = {
        'posts' : Post.objects.all()
    }
    return HttpResponse(template.render(context, request))


def player(request, player_id):
    try :
        play = Player.objects.get(id = player_id)
    except :
        play = None
    
    template = loader.get_template('player.html')
    context = {
        'player' : play
    }
    return HttpResponse(template.render(context, request))

