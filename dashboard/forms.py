from django import forms
from tinymce.widgets import TinyMCE
from newspaper.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ("author", "view_count", "published_at")

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the title of post",
            }),
            "content": TinyMCE(attrs={
                "class": "form-control",
                "placeholder": "Enter the content of post",
            }),
            "status": forms.Select(attrs={
                "class": "form-control",
            }),
            "category": forms.Select(attrs={
                "class": "form-control",
            }),
            "tags": forms.SelectMultiple(attrs={
                "class": "form-control",
            }),
        }
