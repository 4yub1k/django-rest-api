from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('id','author','title','content')
    list_display_links=('id','author','title')


admin.site.register(Post, PostAdmin)
