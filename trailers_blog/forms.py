from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'featured_image', 'excerpt', 'body')
# Python dictionary add many items you like
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your tag here'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
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