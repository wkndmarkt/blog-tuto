from django.contrib import admin
from django.utils.text import Truncator
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display   = ('title','author','created_date','apercu_text')
    list_filter    = ('author',)
    ordering       = ('created_date',)
    search_fields  = ('title','text')
    
    def apercu_text(self, text):
        return Truncator(text).chars(40, truncate='…')

admin.site.register(Post, PostAdmin)
