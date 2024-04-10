from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView,BlogCreateView, BlogUpdateView , BlogDetailView , BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs_list',BlogListView.as_view(),name='blogs_list'),
    path('create_blog',BlogCreateView.as_view(),name='create_blog'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
]