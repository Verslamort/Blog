from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': '', 'title': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
