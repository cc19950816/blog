from django.contrib import admin
from .models import Post, Category, Tag
from comments.models import Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author','views']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','url','text','created_time','post']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

admin.site.register(Comment,CommentAdmin)