from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Topic, Post, Comment


class PostAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'author')


class CommentAdmin(ModelAdmin):
    list_display = ('content', 'created_at', 'contains', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Topic)
admin.site.register(Comment, CommentAdmin)
