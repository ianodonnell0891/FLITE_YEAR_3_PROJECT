from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'newsfeed/home.html', context)

def about(request):
    return render(request, 'newsfeed/about.html', {'title': 'About Melodia'})


