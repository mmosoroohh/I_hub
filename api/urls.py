from django.urls import path
from .views import (
    ListCreateAsset, ListCreateProcessView, ProcessDetailView,
    GroupDetailView, DataClassificationDetailView, ListCreateGroupsView,
    ListCreateDataClassificationView, ListCreateDataMapsView, DataMapsDetailView,
    RegistrationAPIView, LoginAPIView, AssetDetailView, ListCreateDataItemsView,
    DataItemsDetailView, ListCreateDataSubjectView, DataSubjectDetailView, ListCreateSubjectSourceView
)

urlpatterns = [
    path('users/register', RegistrationAPIView.as_view(), name='register-user'),
    path('users/login', LoginAPIView.as_view(), name="login-user"),
    path('assets', ListCreateAsset.as_view(), name="list-create-asset"),
    path('assets/<int:pk>', AssetDetailView.as_view(), name="assets-detail"),
    path('process', ListCreateProcessView.as_view(), name='list-create-process'),
    path('process/<int:pk>', ProcessDetailView.as_view(), name="process-detail"),
    path('groups', ListCreateGroupsView.as_view(), name='list-create-group'),
    path('groups/<int:pk>', GroupDetailView.as_view(), name="group-detail"),
    path('data-classification', ListCreateDataClassificationView.as_view(), name="list-create-dataClassification"),
    path('data-classification/<int:pk>', DataClassificationDetailView.as_view(), name="data-classification-detail"),
    path('data-maps', ListCreateDataMapsView.as_view(), name="list-create-data-maps"),
    path('data-maps/<int:pk>', DataMapsDetailView.as_view(), name="data-maps-details"),
    path('data-items', ListCreateDataItemsView.as_view(), name="list-create-data-items"),
    path('data-items/<int:pk>', DataItemsDetailView.as_view(), name="data-items-detail"),
    path('data-subjects', ListCreateDataSubjectView.as_view(), name="list-create-data-subject"),
    path('data-subjects/<int:pk>', DataSubjectDetailView.as_view(), name="data-inputs-detail"),
    path('reports/<int:src_pk>/test/<int:sub_pk>', ListCreateSubjectSourceView.as_view(), name="list-create-report")
]