from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'featured_image', 'excerpt', 'body')
# Python dictionary add many items you like
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your tag here'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your content'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your content'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'excerpt', 'body')
# Python dictionary add many items you like
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your tag here'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your content'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your content'}),
        }