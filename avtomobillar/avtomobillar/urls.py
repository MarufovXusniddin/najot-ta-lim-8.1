"""
URL configuration for avtomobillar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index, BrandListAPIView, BrandRetrieveAPIView, BrandListCreateAPIView, ModelListAPIView, ModelRetrieveAPIView, ModelListCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('brands_list/v1/', BrandListAPIView.as_view(), name='brands'),
    path('brand/v1/<int:pk>/', BrandRetrieveAPIView.as_view(), name='brand'),
    path('brands/v1/create/', BrandListCreateAPIView.as_view(), name='brands_create'),
    path('models_list/v1/', ModelListAPIView.as_view(), name='models'),
    path('model/v1/<int:pk>/', ModelRetrieveAPIView.as_view(), name='model'),
    path('model/v1/create/', ModelListCreateAPIView.as_view(), name='model_create'),
]
