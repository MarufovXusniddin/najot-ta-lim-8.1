from django.contrib import admin
from .models import Brand, Model

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'pub_date', 'published')
    list_display_links = ('name',)
    list_editable = ('published',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)