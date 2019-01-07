from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields =('title', 'description', 'user')
