from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from blog.models import Post
from blog_api.permissions import IsOwnerOrReadOnly
from blog_api.serializers import PostSerializerList, PostSerializerDetail


class PostListsPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerList
    pagination_class = PostListsPagination
    # permission_classes = (IsOwnerOrReadOnly,)
    # lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        print(self.request.user, 11)
        return self.list(request, *args, **kwargs)


class PostDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDetail
    pagination_class = PostListsPagination
    permission_classes = (IsOwnerOrReadOnly,)


