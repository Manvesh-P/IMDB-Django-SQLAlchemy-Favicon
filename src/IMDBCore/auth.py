from django.contrib.auth import login
from django.contrib.auth.mixins import AccessMixin
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from .utils import init_kwargs
from rest_framework_jwt.authentication import BaseAuthentication, JSONWebTokenAuthentication
import random


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class IMDBLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        #request.user.model contains the cassandra object
        if not request.user.is_authenticated and request.is_ajax():
            return JsonResponse({'error': 'Login required.'}, status=401)
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class IMDBLoginRequiredForWriteMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET': #allow read access
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated and request.is_ajax():
            return JsonResponse({'error': 'Login required.'}, status=401)
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

