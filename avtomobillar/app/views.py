from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView
from .models import Brand, Model
from .serializers import ModelSerializer, BrandSerializer


# Create your views here.


def index(request):
    return render(request, 'index.html')


class BrandsAPIView(APIView):
    def get(self, request: Request) -> Response:
        brands = Brand.objects.all()
        return Response({"brands": BrandSerializer(brands, many=True).data})

    def post(self, request: Request):
        name = request.data['name']
        brand = Brand.objects.create(
            name=name
        )
        return Response({'brand`': model_to_dict(brand),  'message':"Brend qo'shildi!!!"})


class ModelsAPIView(APIView):
    def get(self, request: Request) -> Response:
        models = Model.objects.all()
        return Response({"models": ModelSerializer(models, many=True).data})

    def post(self, request: Request):
        name = request.data['name']
        description = request.data['description']
        category_id = request.data['category_id']
        model = Model.objects.create(
            name=name,
            description=description,
            category_id=category_id
        )
        return Response({'model': model_to_dict(model),  'message':"Model qo'shildi!!!"})



# class BrandListAPIView(ListAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#
# class BrandRetrieveAPIView(RetrieveAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#
# class BrandListCreateAPIView(ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#
# class ModelListAPIView(ListAPIView):
#     queryset = Model.objects.all()
#     serializer_class = ModelSerializer
#
#
# class ModelRetrieveAPIView(RetrieveAPIView):
#     queryset = Model.objects.all()
#     serializer_class = ModelSerializer
#
#
# class ModelListCreateAPIView(ListCreateAPIView):
#     queryset = Model.objects.all()
#     serializer_class = ModelSerializer