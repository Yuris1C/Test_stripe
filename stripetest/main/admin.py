from django.contrib import admin

from main.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "display_price")


admin.site.register(Item, ItemAdmin)
