from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .models import Process, Assets, Groups, DataClassification, DataMaps, DataInputs, Report
from .serializers import AssetSerializer, ProcessSerializer, GroupSerializer, DataClassificationSerializer, DataMapSerializer, DataInputSerializer, ReportSerializer


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
        import pdb;
        pdb.set_trace()
        asset = Assets.objects.create(
            asset_name=request.data["asset_name"],
            location=request.data["location"],
            duration=request.data["duration"],
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


class ListCreateReportsView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def post(self, request, *args, **kwargs):
        report = Report.objects.create(
            report_name=request.data["report_name"],
            record=request.data["record"],
            maps=request.data["maps"]
        )
        return Response(
            data=ReportSerializer(report).data,
            status=status.HTTP_201_CREATED
        )


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get(self, request, *args, **kwargs):
        try:
            report = self.queryset.get(pk=kwargs["pk"])
            return Response(ReportSerializer(report).data)
        except Report.DoesNotExist:
            return Response(
                data={"message": "Report with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            report = self.queryset.get(pk=kwargs["pk"])
            serializer = ReportSerializer()
            update_report = serializer.update(report, request.data)
            return Response(ReportSerializer(update_report).data)
        except Report.DoesNotExist:
            return Response(
                data={"message": "Report with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            report = self.queryset.get(pk=kwargs["pk"])
            report.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Report.DoesNotExist:
            return Response(
                data={"message": "Report with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)


class ListCreateDataInputView(generics.ListAPIView):
    queryset = DataInputs.objects.all()
    serializer_class = DataInputSerializer

    def post(self, request, *args, **kwargs):
        data_inputs = DataInputs.objects.create(
            data_subjects=request.data["data_subjects"],
            data_items=request.data["data_items"],
            data_sources=request.data["data_sources"]
        )
        return Response(
            data=DataInputSerializer(data_inputs).data,
            status=status.HTTP_201_CREATED
        )


class DataInputsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataInputs.objects.all()
    serializer_class = DataInputSerializer

    def get(self, request, *args, **kwargs):
        try:
            data_input = self.queryset.get(pk=kwargs["pk"])
            return Response(DataInputSerializer(data_input).data)
        except DataInputs.DoesNotExist:
            return Response(
                data={"message": "Data input with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            data_input = self.queryset.get(pk=kwargs["pk"])
            serializer = DataInputSerializer()
            update_data = serializer.update(data_input, request.data)
            return Response(DataInputSerializer(update_data).data)
        except DataInputs.DoesNotExist:
            return Response(
                data={"message": "Data input with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            data_input = self.queryset.get(pk=kwargs["pk"])
            data_input.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DataInputs.DoesNotExist:
            return Response(
                data={"message": "Data input with id: {} does not exist".format(kwargs["pk"])},
                status=status.HTTP_404_NOT_FOUND)