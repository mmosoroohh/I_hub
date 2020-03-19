from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from .models import Process, Assets, Groups, DataClassification, DataMaps, DataItems, DataSubject, SubjectSource
from .serializers import AssetSerializer, ProcessSerializer, GroupSerializer, DataClassificationSerializer, \
    DataMapSerializer, UserSerializer, DataItemsSerializer, DataSubjectsSerializer, LoginSerializer



class RegistrationAPIView(generics.CreateAPIView):
    """Register new user"""
    serializer_class = UserSerializer

    def post(self, request):
        request.data['username'] = request.data['username'].lower()
        user = request.data

        serializer = self.serializer_class(
            data=user, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        success_message={
            "success": "User was successfully registered",
            "data": serializer.data
        }
        return Response(success_message, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.CreateAPIView):
    """Login a registered user"""
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        success_message={
            "Success": "Successfully login",
            "data": serializer.data
        }

        return Response(success_message, status=status.HTTP_200_OK)


def get_asset(name):
    try:
        song = Assets.objects.get(name=name)
        return song
    except Assets.DoesNotExist:
        return Response(
            data={"message": "Asset with name: {} does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )


class ListCreateAsset(generics.ListAPIView):
    """Provides a GEt and POST method handler."""
    queryset = Assets.objects.all()
    serializer_class = AssetSerializer

    def post(self, request):
        asset = Assets.objects.create(
            asset_name=request.data["asset_name"],
            location=request.data["location"],
            operator=request.data["operator"],
            process=request.data["process"]
        )
        return Response(data=AssetSerializer(asset).data, status=status.HTTP_201_CREATED)


class AssetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetSerializer

    def get(self, request, *args, **kwargs):
        try:
            asset = self.queryset.get(pk=kwargs["pk"])
            return Response(AssetSerializer(asset).data)
        except Assets.DoesNotExist:
            return Response(
                data={"message": "Asset with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            asset = self.queryset.get(pk=kwargs["pk"])
            serializer = AssetSerializer()
            update_asset = serializer.update(asset, request.data)
            return Response(AssetSerializer(update_asset).data)
        except Assets.DoesNotExist:
            return Response(
                data={"message": "Asset with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            asset = self.queryset.get(pk=kwargs["pk"])
            asset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Assets.DoesNotExist:
            return Response(
                data={"message": "Asset with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateGroupsView(generics.ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer

    def post(self, request, *args, **kwargs):
        group = Groups.objects.create(
            group_name=request.data["group_name"]
        )
        return Response(
            data=GroupSerializer(group).data,
            status=status.HTTP_201_CREATED
        )


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer

    def get(self, request, *args, **kwargs):
        try:
            group = self.queryset.get(pk=kwargs["pk"])
            return Response(GroupSerializer(group).data)
        except Groups.DoesNotExist:
            return Response(
                data={"message": "Group with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            group = self.queryset.get(pk=kwargs["pk"])
            serializer = GroupSerializer()
            update_group = serializer.update(group, request.data)
            return Response(ProcessSerializer(update_group).data)
        except Groups.DoesNotExist:
            return Response(
                data={"message": "Group with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            group = self.queryset.get(pk=kwargs["pk"])
            group.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Groups.DoesNotExist:
            return Response(
                data={"message": "Group with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)


class ListCreateProcessView(generics.ListAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    def post(self, request, *args, **kwargs):
        process = Process.objects.create(
            process_name=request.data["process_name"],
            owner=request.data["owner"]
        )
        return Response(
            data=ProcessSerializer(process).data,
            status=status.HTTP_201_CREATED
        )


class ProcessDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    def get(self, request, *args, **kwargs):
        try:
            process = self.queryset.get(pk=kwargs["pk"])
            return Response(ProcessSerializer(process).data)
        except Process.DoesNotExist:
            return Response(
                data={"message": "Process with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            process = self.queryset.get(pk=kwargs["pk"])
            serializer = ProcessSerializer()
            update_process = serializer.update(process, request.data)
            return Response(ProcessSerializer(update_process).data)
        except Process.DoesNotExist:
            return Response(
                data={"message": "Process with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            process = self.queryset.get(pk=kwargs["pk"])
            process.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Process.DoesNotExist:
            return Response(
                data={"message": "Process with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)


class ListCreateDataClassificationView(generics.ListAPIView):
    queryset = DataClassification.objects.all()
    serializer_class = DataClassificationSerializer

    def post(self, request, *args, **kwargs):
        data_classification = DataClassification.objects.create(
            data_name=request.data["data_name"],
            description=request.data["description"]
        )
        return Response(
            data=DataClassificationSerializer(data_classification).data,
            status=status.HTTP_201_CREATED
        )


class DataClassificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataClassification.objects.all()
    serializer_class = DataClassificationSerializer

    def get(self, request, *args, **kwargs):
        try:
            dataClassification = self.queryset.get(pk=kwargs["pk"])
            return Response(ProcessSerializer(dataClassification).data)
        except DataClassification.DoesNotExist:
            return Response(
                data={"message": "Data Classification with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            dataClassification = self.queryset.get(pk=kwargs["pk"])
            serializer = DataClassificationSerializer()
            update_data = serializer.update(dataClassification, request.data)
            return Response(ProcessSerializer(update_data).data)
        except DataClassification.DoesNotExist:
            return Response(
                data={"message": "Data Classification  with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            dataClassification = self.queryset.get(pk=kwargs["pk"])
            dataClassification.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DataClassification.DoesNotExist:
            return Response(
                data={"message": "Data Classification with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)


class ListCreateDataMapsView(generics.ListAPIView):
    queryset = DataMaps.objects.all()
    serializer_class = DataMapSerializer

    def post(self, request, *args, **kwargs):
        data_maps = DataMaps.objects.create(
            image=request.data["image"],
            name=request.data["name"]
        )
        return Response(
            data=DataMapSerializer(data_maps).data,
            status=status.HTTP_201_CREATED
        )


class DataMapsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataMaps.objects.all()
    serializer_class = DataMapSerializer

    def get(self, request, *args, **kwargs):
        try:
            data_maps = self.queryset.get(pk=kwargs["pk"])
            return Response(DataMapSerializer(data_maps).data)
        except DataMaps.DoesNotExist:
            return Response(
                data={"message": "Data Maps with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            data_maps = self.queryset.get(pk=kwargs["pk"])
            serializer = DataMapSerializer()
            update_maps = serializer.update(data_maps, request.data)
            return Response(DataMapSerializer(update_maps).data)
        except DataMaps.DoesNotExist:
            return Response(
                data={"message": "Data Maps  with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            data_maps = self.queryset.get(pk=kwargs["pk"])
            data_maps.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DataMaps.DoesNotExist:
            return Response(
                data={"message": "Data Maps with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)


class ListCreateDataItemsView(generics.ListAPIView):
    queryset = DataItems.objects.all()
    serializer_class = DataItemsSerializer

    def post(self, request, *args, **kwargs):
        item = DataItems.objects.create(
            name=request.data["name"],
        )
        return Response(
            data=DataItemsSerializer(item).data,
            status=status.HTTP_201_CREATED
        )


class DataItemsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataItems.objects.all()
    serializer_class = DataItemsSerializer

    def get(self, request, *args, **kwargs):
        try:
            item = self.queryset.get(pk=kwargs["pk"])
            return Response(DataItemsSerializer(item).data)
        except DataItems.DoesNotExist:
            return Response(
                data={"message": "Data item with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            item = self.queryset.get(pk=kwargs["pk"])
            serializer = DataItemsSerializer()
            update_item = serializer.update(item, request.data)
            return Response(DataItemsSerializer(update_item).data)
        except DataItems.DoesNotExist:
            return Response(
                data={"message": "Data item with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            item = self.queryset.get(pk=kwargs["pk"])
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DataItems.DoesNotExist:
            return Response(
                data={"message": "Data item with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)


class ListCreateDataSubjectView(generics.ListAPIView):
    queryset = DataSubject.objects.all()
    serializer_class = DataSubjectsSerializer

    def post(self, request, *args, **kwargs):
        data_subject = DataSubject.objects.create(
            name=request.data["name"],
        )
        return Response(
            data=DataSubjectsSerializer(data_subject).data,
            status=status.HTTP_201_CREATED
        )


class DataSubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataSubject.objects.all()
    serializer_class = DataSubjectsSerializer

    def get(self, request, *args, **kwargs):
        try:
            data_subject = self.queryset.get(pk=kwargs["pk"])
            return Response(DataSubjectsSerializer(data_subject).data)
        except DataSubject.DoesNotExist:
            return Response(
                data={"message": "Data subject with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            data_subject = self.queryset.get(pk=kwargs["pk"])
            serializer = DataSubjectsSerializer()
            update_subject = serializer.update(data_subject, request.data)
            return Response(DataSubjectsSerializer(update_subject).data)
        except DataSubject.DoesNotExist:
            return Response(
                data={"message": "Data subject with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            data_subject = self.queryset.get(pk=kwargs["pk"])
            data_subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DataSubject.DoesNotExist:
            return Response(
                data={"message": "Data subject with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)
