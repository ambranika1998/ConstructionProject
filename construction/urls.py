from django.urls import path

from construction.views import UserListAPIView

USER_LIST = 'user-list'


urlpatterns = [
    path('user-list/', UserListAPIView.as_view(), name=USER_LIST),
    ]
