from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')


def about(request):
    return render(request, 'portfolio/about.html')


def gallery(request):
    images = [f"images/gallery{i}.jpg" for i in range(1, 21)]
    return render(request, 'portfolio/gallery.html', {'images': images})


def services(request):
    return render(request, 'portfolio/services.html')


def contact(request):
    return render(request, 'portfolio/contact.html')