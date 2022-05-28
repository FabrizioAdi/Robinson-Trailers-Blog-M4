from django.urls import path
from . import views
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView, LikeView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
]