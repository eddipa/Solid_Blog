from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView
from .views import PostMonthView
from .views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView
from .views import TagListView, TagDetailView, TagCreateView, TagDeleteView, TagUpdateView
from .views import AuthorListView, AuthorDetailView

urlpatterns = [
    # post
    path('', PostListView.as_view(), name='post_list'),
    path('post/view/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/update/<slug:slug>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),
    # # months
    path('post/archive/<str:month>', PostMonthView.as_view(), name='post_month'),
    # tag
    path('tag', TagListView.as_view(), name='tag_list'),
    path('tag/view/<slug:slug>', TagDetailView.as_view(), name='tag_detail'),
    path('tag/create', TagCreateView.as_view(), name='tag_create'),
    path('tag/update/<slug:slug>', TagUpdateView.as_view(), name='tag_update'),
    path('tag/delete/<slug:slug>', TagDeleteView.as_view(), name='tag_delete'),
    # category
    path('category', CategoryListView.as_view(), name='category_list'),
    path('category/view/<slug:slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<slug:slug>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<slug:slug>', CategoryDeleteView.as_view(), name='category_delete'),
    # author
    path('author', AuthorListView.as_view(), name='author_list'),
    path('author/<slug:slug>', AuthorDetailView.as_view(), name='author_detail'),
]
