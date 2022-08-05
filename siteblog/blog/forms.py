from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class CreatePost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title","author","category","content","tags","slug","image",)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }