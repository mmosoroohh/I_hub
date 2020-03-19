from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Assets, Groups, DataClassification, Process, DataMaps, DataSubject, DataItems, SubjectSource, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


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
