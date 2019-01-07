import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
from oauth2_provider.views import TokenView, RevokeTokenView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import RegistrationSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
           Register users by username and password
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomTokenView(TokenView):

    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        """
          Generate user's access token
        """
        url, headers, body, status = self.create_token_response(request)
        content = {}
        if status == 200:
            access_token = json.loads(body).get("access_token")
            if access_token is not None:
                token = get_access_token_model().objects.get(
                    token=access_token)
                app_authorized.send(
                    sender=self, request=request,
                    token=token)

                # Only access_token in response
                content = {'access_token': access_token}

        return HttpResponse(content=json.dumps(content), status=status)


class CustomRevokeTokenView(RevokeTokenView):
    def post(self, request, *args, **kwargs):
        """
         Log off by revoking user's access token
        """
        url, headers, body, status = self.create_revocation_response(request)

        body = json.loads(body) if body else {}
        body['success'] = True if status == 200 else False
        response = HttpResponse(content=json.dumps(body) or "", status=status)

        for k, v in headers.items():
            response[k] = v
        return response