from django.shortcuts import render
from drink.models import Drink
from django.http import response, JsonResponse
from drink.serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status



@api_view(['POST', 'GET'])
def drink_list(request, format=None):
    #get all drink
    #serialize them
    #return JSON
    if request.method == 'GET':
        drink_list = Drink.objects.all()
        serializer = DrinkSerializer(drink_list, many=True)
        return JsonResponse({'drinks': serializer.data})
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk, format=None):
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return JsonResponse({'error': 'Drink not found'}, status=404)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        drink.delete()
        return JsonResponse({'message': 'Drink deleted successfully'}, status=204)