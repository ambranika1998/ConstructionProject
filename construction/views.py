from rest_framework import generics

from construction.filters import UserFilter
from construction.models import User
from construction.serializers import UserSerializer


# Create your views here.
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
