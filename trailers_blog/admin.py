from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(Post)
admin.site.register(Category)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)