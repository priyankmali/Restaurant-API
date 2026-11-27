from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from restaurants.models import*
from restaurants.serializers import*
from rest_framework import serializers
from rest_framework import status

# Create your views here.
class getPostRestaurant(APIView):

    def get(self,reqeust):
        restaurant=Restaurant.objects.all()
        ser=RestaurantSerializer(restaurant,many=True)
        return Response({'data':ser.data}, status=status.HTTP_200_OK)

    def post(self,request):
        ser=RestaurantSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':ser.errors},status=status.HTTP_400_BAD_REQUEST)

class gByIDPuPatDel_Restaurant(APIView):

    def get(self,request,id):
        try:
            restaurant=Restaurant.objects.get(pk=id)
            ser=RestaurantSerializer(restaurant)
            return Response({'data':ser.data},status=status.HTTP_200_OK)
        except:
            return Response({'errors':ser.errors},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        restaurant=Restaurant.objects.get(pk=id)
        ser=RestaurantSerializer(restaurant,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data},status=status.HTTP_200_OK)
        else:
            return Response({'errors':ser.errors},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        restaurant=Restaurant.objects.get(pk=id)
        ser=RestaurantSerializer(restaurant,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data},status=status.HTTP_200_OK)
        else:
            return Response({'errors':ser.errors},status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,reqeust,id):
        restaurant=Restaurant.objects.get(pk=id)
        restaurant.delete()
        return Response({'msg':'successfully deleted resturant..'},status=status.HTTP_200_OK)



        

    
        
