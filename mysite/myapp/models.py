from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    prefers = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Post(models.Model):
    slug = models.SlugField(max_length=36)
    title = models.CharField(max_length=128)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    contains = models.ManyToManyField(Topic)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    contains = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
# class Article(models.Model):
#     name = models.CharField(max_length=100)
#     text = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name


# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.utils.translation import gettext as _
#
# GENRE_CHOICES = (
#     (1, _("Not selected")),
#     (2, _("Comedy")),
#     (3, _("Action")),
#     (4, _("Beauty")),
#     (5, _("Other"))
# )
#
#
# class Author(models.Model):
#     pseudonym = models.CharField(max_length=120, blank=True, null=True)
#     name = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.name
#
#
# class Article(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='articles')
#     text = models.TextField(max_length=10000, null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
#     genre = models.IntegerField(choices=GENRE_CHOICES, default=1)
#
#     def __str__(self):
#         return "Author - {}, genre - {}, id - {}".format(self.author.name, self.genre, self.id)
#
#
# class Comment(models.Model):
#     text = models.CharField(max_length=1000)
#     article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
#     comment = models.ForeignKey('myapp.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
#                                 related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return "{} by {}".format(self.text, self.user.username)
#
#
# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return "By user {} to article {}".format(self.user.username, self.article.id)
