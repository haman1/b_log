from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Arme',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'articles/home.html', context)


def about(request):
    return render(request, 'articles/about.html', {'title': 'About'})