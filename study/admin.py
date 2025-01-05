from django.contrib import admin
from .models import *

# Register your models here.
class notes_(admin.ModelAdmin):
    list_display=('user','title','dis')

admin.site.register(notes,notes_)


# Register your models here.
class works_(admin.ModelAdmin):
    list_display=('user','title','dis','due','subject','is_finished')

admin.site.register(work,works_)


class todo_(admin.ModelAdmin):
    list_display=('user','title','is_finished')

admin.site.register(todoo,todo_)

