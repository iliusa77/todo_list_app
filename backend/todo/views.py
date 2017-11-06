from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# my import
from .serializers import UserSerializer, GroupSerializer, TaskSerializer, GroupTaskSerializer
from .models import Task, GroupTask

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# ViewSet Approach (3 layer)
# class TaskViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows tasks to be viewed or edited.
#     """
#     pagination_class = LimitOffsetPagination
#     permission_classes = []
#     queryset = Task.objects.select_related('group').all()
#     serializer_class = TaskSerializer

# class GroupTaskViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows group tasks to be viewed or edited.
#     """
#     pagination_class = LimitOffsetPagination
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = GroupTask.objects.all()
#     serializer_class = GroupTaskSerializer


# Generic Viewes Approach (2 layer)
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

class TaskListView(ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Task.objects.select_related('group').all()
    serializer_class = TaskSerializer


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Task.objects.select_related('group').all()
    serializer_class = TaskSerializer

class GroupListView(ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = GroupTask.objects.all()
    serializer_class = GroupTaskSerializer

class GroupListDetailView(RetrieveUpdateDestroyAPIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = GroupTask.objects.all()
    serializer_class = GroupTaskSerializer

# ApiViewes Approach (1 layer)


