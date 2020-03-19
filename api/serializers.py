from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Assets, Groups, DataClassification, Process, DataMaps, Report, DataInputs


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


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class DataInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataInputs
        fields = '__all__'
