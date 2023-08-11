from django.http import JsonResponse
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def recipe_list(request, format = None):
    
  if request.method == 'GET':
      recipe = Recipe.objects.all()
      serializer = RecipeSerializer(recipe, many=True)
      return JsonResponse(serializer.data, safe=False)
    
  if request.method == 'POST':
      serializer = RecipeSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])    
def recipe_details(request, id, format = None):

  try:
    recipe = Recipe.objects.get(pk = id)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = RecipeSerializer(recipe, data = request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
  elif request.method == 'DELETE':
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
           
    