from rest_framework import generics

from construction.filters import UserFilter, ConstructionSiteFilter, TrellisFilter, JobFilter, JobUserFilter
from construction.models import User, ConstructionSite, Trellis, Job, JobUser
from construction.serializers import UserSerializer, ConstructionSiteSerializer, TrellisSerializer, JobSerializer, \
    JobUserSerializer


# Create your views here.
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    def get_queryset(self):
        return self.queryset.distinct()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConstructionSiteListCreateAPIView(generics.ListCreateAPIView):
    queryset = ConstructionSite.objects.all()
    serializer_class = ConstructionSiteSerializer
    filterset_class = ConstructionSiteFilter


class ConstructionSiteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConstructionSite.objects.all()
    serializer_class = ConstructionSiteSerializer


class TrellisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Trellis.objects.all()
    serializer_class = TrellisSerializer
    filterset_class = TrellisFilter


class TrellisRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trellis.objects.all()
    serializer_class = TrellisSerializer


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filterset_class = JobFilter


class JobRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobUser.objects.all()
    serializer_class = JobUserSerializer
    filterset_class = JobUserFilter


class JobUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobUser.objects.all()
    serializer_class = JobUserSerializer
