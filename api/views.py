from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from api.models import Food


class FoodSerializer(ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'


@api_view(['GET'])
def get_foods(request):
    page = request.query_params.get('page', 0)
    content_per_page = 20

    start_index = (page * content_per_page)
    end_index = content_per_page + start_index - 1

    foods = Food.objects.all()[start_index:end_index]
    data = FoodSerializer(foods, many=True).data

    return Response(data)


@api_view(['GET'])
def download(request):
    food_id = request.query_params.get('food', None)
    if food_id:
        try:
            food = Food.objects.get(pk=food_id)
            food.popularity += 1
            food.save()
        except Food.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response()



