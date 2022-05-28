from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
# return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']
    #ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

# Functional view
def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat)
    return render(request, 'categories.html', {'cat':cat.title(), 'category_posts':category_posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        count = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = count.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    # Method to add separately
    #fields = ('title', 'author', 'featured_image', 'excerpt', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    #fields = ('title', 'title_tag', 'featured_image', 'excerpt', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

# Likes function
def LikeView(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
