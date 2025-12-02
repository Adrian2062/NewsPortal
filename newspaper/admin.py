from django.contrib import admin
from newspaper.models import Newsletter, Post, Tag, Category, Advertisement, Contact, OurTeam, Comment, UserProfile
# Register your models here.
#admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(Contact)
admin.site.register(OurTeam)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Newsletter)

from django import forms
from tinymce.widgets import TinyMCE
from unfold.admin import ModelAdmin


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'status', 'published_at')
    list_filter = ('status', 'category', 'author')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
