from rest_framework import serializers
from accounts.serializers import UserSerializer

from accounts.models import User
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # UserSerializer gives extra user's fields
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('title', 'description', 'user')


class AddCommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ('title', 'description', 'user')
