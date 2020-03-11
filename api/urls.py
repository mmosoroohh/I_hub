from django.urls import path
from .views import (
    ListCreateAsset, ListCreateProcessView, ProcessDetailView
)

urlpatterns = [
    path('assets', ListCreateAsset.as_view(), name="list-create-asset"),
    path('process', ListCreateProcessView.as_view(), name='list-create-process'),
    path('process/<int:pk>', ProcessDetailView.as_view(), name="process-detail"),
]