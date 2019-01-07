from django.conf.urls import url

from .views import RegistrationAPIView, CustomTokenView, CustomRevokeTokenView

urlpatterns = [
    url(r'^register/?$', RegistrationAPIView.as_view()),
    url(r'^o/token/?$', CustomTokenView.as_view()),
    url(r'^o/revoke_token/?$', CustomRevokeTokenView.as_view()),
]
