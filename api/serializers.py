from abc import ABC

from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import Assets, Groups, DataClassification, Process, DataMaps, DataSubject, DataItems, SubjectSource, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'Username required to log in'
            )
        if password is None:
            raise serializers.ValidationError(
                'Password required to log in'
            )

        return {
            'username': username
        }


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class DataClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataClassification
        fields = '__all__'


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'


class DataMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataMaps
        fields = '__all__'


class DataSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSubject
        fields = '__all__'


class DataItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataItems
        fields = '__all__'


class SubjectSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectSource
        fields = '__all__'
