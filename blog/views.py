from django.shortcuts import render


posts = [
    {
        "author": "Cedric Bansah",
        "title": "Django for Beginners",
        "content": "First page of book",
        "date_posted": "May 28"
    },
    {
        "author": "Kendall Roy",
        "title": "Little Lord Fuckleroy",
        "content": "One head one crown. Reverse Viking",
        "date_posted": "May 28"
    }
]
def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})