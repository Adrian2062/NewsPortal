from django.contrib import admin
from newspaper.models import Post, Tag, Category, Advertisement, Contact, OurTeam, Comment, UserProfile
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(Contact)
admin.site.register(OurTeam)
admin.site.register(Comment)
admin.site.register(UserProfile)