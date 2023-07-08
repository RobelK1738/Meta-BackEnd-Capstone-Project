from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, MenuItems
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets, generics

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class BookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class MenuView(APIView):    
    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ "status": "success", "data": serializer.data })
        
        
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        menu_item = get_object_or_404(MenuItems, pk=pk)
        data = {
            'id': menu_item.pk,
            'title': menu_item.Title,
        }
        return JsonResponse(data)

    def put(self, request, pk):
        menu_item = get_object_or_404(MenuItems, pk=pk)
        menu_item.Title = request.POST.get('name')
        menu_item.save()
        return JsonResponse({'message': 'Menu item updated successfully'})

    def delete(self, request, pk):
        menu_item = get_object_or_404(MenuItems, pk=pk)
        menu_item.delete()
        return JsonResponse({'message': 'Menu item deleted successfully'})
