from django.urls import path, include
from rest_framework import routers

from blog_api.views import PostListView, PostDetailView, PostPhotoView

router = routers.SimpleRouter()
router.register(r'posts', PostDetailView, basename='post')
router.register(r'posts/photo', PostPhotoView, basename='post')



urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('', include(router.urls)),
    # path('posts/<int:pk>', PostDetailView.as_view(), name='post-list')
]
