from django.contrib import admin
from main.models import Information

# Register your models here.


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'password')
    