from django.contrib import admin
from .models import Category, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ('name', 'description', 'price', 'image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_count')
    inlines = [MenuItemInline]

    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = "Items"


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')
