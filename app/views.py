from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from app.models import Posts

def index(request):
    posts = Posts.objects.order_by('-modified')[:20]
    template = loader.get_template('posts/index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    try:
        post = Posts.objects.get(pk=post_id)
    except Posts.DoesNotExist:
        raise Http404("Question does not exist")

    template = loader.get_template('posts/detail.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))

