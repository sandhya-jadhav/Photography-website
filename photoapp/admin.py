from django.contrib import admin
from .models import Category, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    search_fields = ('title', 'category__name')
    list_filter = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
