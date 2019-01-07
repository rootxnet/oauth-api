from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions, generics, views, status, mixins
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    queryset = Comment.objects.all()

    def post(self, request, **kwargs):
        request.POST._mutable = True

        data = request.data
        data['user'] = request.user.id
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
