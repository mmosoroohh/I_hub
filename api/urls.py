from django.urls import path
from .views import (
    ListCreateAsset, ListCreateProcessView, ProcessDetailView,
    GroupDetailView, DataClassificationDetailView, ListCreateGroupsView,
    ListCreateDataClassificationView, ListCreateDataMapsView, DataMapsDetailView,
    ListCreateReportsView, ReportDetailView, ListCreateDataInputView, DataInputsDetailView,
    RegistrationAPIView, LoginAPIView
)

urlpatterns = [
    path('assets', ListCreateAsset.as_view(), name="list-create-asset"),
    path('process', ListCreateProcessView.as_view(), name='list-create-process'),
    path('process/<int:pk>', ProcessDetailView.as_view(), name="process-detail"),
    path('groups', ListCreateGroupsView.as_view(), name='list-create-group'),
    path('groups/<int:pk>', GroupDetailView.as_view(), name="group-detail"),
    path('data-classification', ListCreateDataClassificationView.as_view(), name="list-create-dataClassification"),
    path('data-classification/<int:pk>', DataClassificationDetailView.as_view(), name="data-classification-detail"),
    path('data-maps', ListCreateDataMapsView.as_view(), name="list-create-data-maps"),
    path('data-maps/<int:pk>', DataMapsDetailView.as_view(), name="data-maps-details"),
    path('reports', ListCreateReportsView.as_view(), name="list-create-reports"),
    path('reports/<int:pk>', ReportDetailView.as_view(), name="report-detail"),
    path('data-inputs', ListCreateDataInputView.as_view(), name="list-create-data-inputs"),
    path('data-inputs/<int:pk>', DataInputsDetailView.as_view(), name="data-inputs-detail"),
    path('users/register', RegistrationAPIView.as_view(), name='register-user'),
    path('users/login', LoginAPIView.as_view(), name="login-user")
]