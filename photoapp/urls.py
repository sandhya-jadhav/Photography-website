from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/category/<int:category_id>/', views.gallery, name='gallery_by_category'),

    



]
