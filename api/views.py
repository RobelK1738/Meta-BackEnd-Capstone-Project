from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Booking.objects.all()