from django.shortcuts import render


posts = [
    {
        "author": "Cedric Bansah",
        "title": "Amapiano Will Never Die",
        "content": "SUKA!!",
        "date_posted": "May 28"
    },
    {
        "author": "Kendall Roy",
        "title": "Little Lord Fuckleroy",
        "content": "One head one crow. Reverse Viking",
        "date_posted": "May 2"
    }
]
def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})