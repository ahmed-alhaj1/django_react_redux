from django.shortcuts import render
from rest_auth.views import (LoginView , LogoutView)

from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated 



# Create your views here.

class APILogoutView(LogoutView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class APILoginView(LoginView):

    pass


