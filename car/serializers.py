from rest_framework import serializers
from .models import Car,Detail,Detail_Type,Extra

class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ('id','detail_key','detail_value')

class DetailTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail_Type
        fields = ('id','type_name')

class DetailSerializer(serializers.ModelSerializer):
    detail_type = DetailTypeSerializer('detail_type')
    extras = ExtraSerializer('extras', many=True)
    class Meta:
        model = Detail
        fields = ('id','detail_type','price','quantity','total_price','extras')

class CarSerializer(serializers.ModelSerializer):
    details = DetailSerializer('details', many=True)
    class Meta:
        model = Car
        fields = ('id','name','manufacturer_charge','price','details')