# keerthanajohn
# sapor3456

from django.contrib import admin
from.models import SliderImage,Menu,ContactMessage


class sliderAdmin(admin.ModelAdmin):
    list_display =("image","title",)
admin.site.register(SliderImage)

class FoodAdmin(admin.ModelAdmin):
    list_display =("image","name","price","quantity","description",)
admin.site.register(Menu)

class ContactAdmin(admin.ModelAdmin):
    list_display=("name","email","subject","message","created_at")
admin.site.register(ContactMessage)