from django.contrib import admin
from .models import CustomUser, Contact, About
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    list_display_links = ('id', 'image', 'created_at')


admin.site.register(CustomUser)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact)
