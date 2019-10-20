from django.shortcuts import render


def home(request):
    return render(request, 'resturant/home.html', {'body_class': 'homepage'})

def about(request):
    return render(request, 'resturant/about.html')

def contact(request):
    return render(request, 'resturant/contact.html')

def menu(request):
    return render(request, 'resturant/menu.html')

def gallery(request):
    return render(request, 'resturant/gallery.html')

def catering(request):
    return render(request, 'resturant/catering.html')