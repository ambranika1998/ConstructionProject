from django.urls import path
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from construction.views import UserListCreateAPIView, ConstructionSiteListCreateAPIView, \
    ConstructionSiteRetrieveUpdateDestroyAPIView, TrellisListCreateAPIView, TrellisRetrieveUpdateDestroyAPIView, \
    JobListCreateAPIView, JobRetrieveUpdateDestroyAPIView, JobUserListCreateAPIView, JobUserRetrieveUpdateDestroyAPIView

USER_LIST = 'user'
CONSTRUCTION_SITE = 'construction-site'
TRELLIS = 'trellis'
JOB = 'job'
JOB_USER = 'job-user'

urlpatterns = [
    path('user/', UserListCreateAPIView.as_view(), name=USER_LIST),
    path('user/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(), name=USER_LIST),
    path('construction-site/', ConstructionSiteListCreateAPIView.as_view(), name=CONSTRUCTION_SITE),
    path('construction-site/<int:pk>/', ConstructionSiteRetrieveUpdateDestroyAPIView.as_view(), name=CONSTRUCTION_SITE),
    path('trellis/', TrellisListCreateAPIView.as_view(), name=TRELLIS),
    path('trellis/<int:pk>/', TrellisRetrieveUpdateDestroyAPIView.as_view(), name=TRELLIS),
    path('job/', JobListCreateAPIView.as_view(), name=JOB),
    path('job/<int:pk>/', JobRetrieveUpdateDestroyAPIView.as_view(), name=JOB),
    path('job-user/', JobUserListCreateAPIView.as_view(), name=JOB_USER),
    path('job-user/<int:pk>/', JobUserRetrieveUpdateDestroyAPIView.as_view(), name=JOB_USER),
    ]
