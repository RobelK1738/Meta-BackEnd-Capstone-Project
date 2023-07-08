from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, MenuItems
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer

from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, generics

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class MenuView(APIView):    
    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ "status": "success", "data": serializer.data })
        
        
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer