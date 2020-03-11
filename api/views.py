from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .models import Process, Assets
from .serializers import AssetSerializer, ProcessSerializer


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
            asset_name = request.data["asset_name"],
            location = request.data["location"],
            duration = request.data["duration"],
            process = request.data["process"]
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


class ListCreateProcessView(generics.ListAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    def post(self, request, *args, **kwargs):
        process = Process.objects.create(
            process_name = request.data["process_name"],
            owner = request.data["owner"]
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
                serializer=ProcessSerializer()
                update_process= serializer.update(process, request.data)
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


# class RegisterUsers(generics.CreateAPIView):
#     """
#     POST users/register/
#     """
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = UserSerializer
#
#     def post(self, request, *args, **kwargs):
#         request.data['username'] = request.data['username'].lower()
#         user = request.data
#         serializer = self.serializer_class(
#             data=user, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             serializer.data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# class LoginView(generics.CreateAPIView):
#     """
#     POST users/login/
#     """
#
#     # This permission class will over ride the global permission
#     # class setting
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)



