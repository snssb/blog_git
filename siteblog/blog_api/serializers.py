from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post


class PostSerializerList(serializers.ModelSerializer):
    # author_l = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    author_l = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # lookup_field = 'slug'

    class Meta:
        model = Post
        fields = ('title', 'author_l', 'content', 'created_at')


class PostSerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
