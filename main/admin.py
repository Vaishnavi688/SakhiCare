from django.contrib import admin

# Register your models here.
# main/admin.py
from django.contrib import admin
from .models import Category, CategoryItem

class ItemInline(admin.TabularInline):
    model = CategoryItem
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(CategoryItem)
