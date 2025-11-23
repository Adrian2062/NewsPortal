from django.contrib import admin
from newspaper.models import Post, Tag, Category, Advertisement
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)