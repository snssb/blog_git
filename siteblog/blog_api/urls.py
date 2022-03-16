from django.urls import path, include
from rest_framework import routers

from blog_api.views import PostListView, PostDetailView


router = routers.SimpleRouter()
router.register(r'posts', PostDetailView)



urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('', include(router.urls)),
    # path('posts/<int:pk>', PostDetailView.as_view(), name='post-list')
]
