from django.conf.urls import url
from comments.views import CommentListView

urlpatterns = [
    url(r'^comments/?$', CommentListView.as_view()),
]