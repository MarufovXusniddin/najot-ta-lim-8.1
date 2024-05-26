from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from .models import Brand, Model
from .serializers import BrandSerializer, ModelSerializer

# Create your views here.


def index(request):
    return render(request, 'index.html')


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandListCreateAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ModelListAPIView(ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ModelRetrieveAPIView(RetrieveAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ModelListCreateAPIView(ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer