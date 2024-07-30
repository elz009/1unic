from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkModel
from .serializers import WorkModelSerializer

from category import models, serializers


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    pagination_class = None


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.DistrictSerializerGet
        else:
            return serializers.DistrictSerializer


class IndicatorCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.IndicatorCategory.objects.all().order_by('id')
    serializer_class = serializers.IndicatorCategorySerializer
    pagination_class = None


class IndicatorSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.IndicatorSubCategory.objects.all().order_by('id')
    serializer_class = serializers.IndicatorSubCategorySerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.IndicatorSubCategorySerializerGet
        else:
            return serializers.IndicatorSubCategorySerializer


class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.NewsCategory.objects.all()
    serializer_class = serializers.NewsCategorySerializer
    pagination_class = None


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    pagination_class = None


class GraphCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.GraphCategory.objects.all()
    serializer_class = serializers.GraphCategorySerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.GraphCategorySerializerGet
        else:
            return serializers.GraphCategorySerializer

class WorkModelViewSet(viewsets.ModelViewSet):
    queryset = WorkModel.objects.all()
    serializer_class = WorkModelSerializer