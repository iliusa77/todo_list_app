#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Task, GroupTask


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TaskSerializer(serializers.ModelSerializer):

    group_name = serializers.CharField(source='group.name', read_only=True)
    # custom = serializers.SerializerMethodField(method_name='foo')
    #
    # def foo(self, instance):
    #     return 'hello'

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'description',
            'group',
            'group_id',
            'group_name',
            #'custom'
        ]

class GroupTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupTask
        fields = [
            'id',
            'name',
        ]