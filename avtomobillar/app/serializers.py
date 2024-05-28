import io
from datetime import datetime

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class ModelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    category_id = serializers.IntegerField()
    pub_date = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=False)


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)












# Serializatsiya va deserializatsiya

# class Model:
#     def __init__(self, name, description, pub_date, published):
#         self.name = name
#         self.description = description
#         self.pub_date = pub_date or datetime.now()
#         self.published = published


# def serialization():
#     model1 = Model('Gentra','Lorem', '',True)
#     serializer = ModelSerializer(model1)
#     print(serializer.data)
#
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#     print(type(json))
#
#
# def deserialization():
#     json = b'{"name":"Nimadir","description":"Lorem"}'
#     stream = io.BytesIO(json)
#     data = JSONRenderer().parse(stream)
#     print(data, 'Json parser obyekti')
#
#     serializer = ModelSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)














# class BrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brand
#         fields = '__all__'
#
#
# class ModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Model
#         fields = '__all__'
