from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sentences
from .models import Tags
from .models import Sentence_Tag
# Register your models here.


class MyCustomAdmin(admin.ModelAdmin):
    list_display = ['sentence']

admin.site.register(Sentences, MyCustomAdmin)

class MyCustomAdmin(admin.ModelAdmin):
    list_display = ['name','description']

admin.site.register(Tags, MyCustomAdmin)

class MyCustomAdmin(admin.ModelAdmin):
    list_display = ['sentence','tag','word']

admin.site.register(Sentence_Tag, MyCustomAdmin)