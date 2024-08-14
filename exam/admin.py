from django.contrib import admin
from .models import CustomUser, Contact, About, TurPaket, Image
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    list_display_links = ('id', 'image', 'created_at')


class TurPaketAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_Name', 'u_sana', 'q_sana', 'hotel_name')
    list_display_links = ('id', 'city_Name', 'u_sana', 'q_sana', 'hotel_name')


admin.site.register(CustomUser)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact)
admin.site.register(TurPaket, TurPaketAdmin)
admin.site.register(Image)
