from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from app.models import Posts

def index(request):
    posts = Posts
    template = loader.get_template('posts/index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))