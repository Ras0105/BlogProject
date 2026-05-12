from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Write your comment...',
                'rows': 3,
            })
        }
        labels = {
            'text': 'Comment'
        }
