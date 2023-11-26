from django.contrib import admin
from .models import pizza


class pizza_Admin(admin.ModelAdmin):
    list_display = ("name","ingridients","price","vegetarian")
    search_fields = ["name"]
# Register your models here.
admin.site.register(pizza,pizza_Admin)