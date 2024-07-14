from django.shortcuts import render,get_object_or_404
from .models import Category, Photo


def home(request):
    return render(request, 'photoapp/home.html')

# def gallery(request):
#     categories = Category.objects.all()
#     return render(request, 'photoapp/gallery.html', {'categories': categories})

# def gallery(request):
#     photos = Photo.objects.all()
#     return render(request, 'photoapp/gallery.html', {'photos': photos})


def gallery(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        photos = Photo.objects.filter(category=category)
    else:
        photos = Photo.objects.all()
    categories = Category.objects.all()
    context = {
        'photos': photos,
        'categories': categories,
        'selected_category': category_id,
    }
    return render(request, 'photoapp/gallery.html', context)


def about(request):
    return render(request, 'photoapp/about.html')

def contact(request):
    return render(request, 'photoapp/contact.html')

