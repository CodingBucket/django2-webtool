from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Home View</h1>")
    return render(request, "pages/home.html", {})

def contact_view(request):
    my_context = {
        "title": "capfirst letter",
        "my_text": "This is about us",
        "my_num": 123,
        "my_list": [1, 2, 3, 4]
    }
    return render(request, "pages/contact.html", my_context)

def about_view(request):
    return HttpResponse("<h1>About View</h1>")
