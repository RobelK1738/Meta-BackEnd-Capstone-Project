from django.urls import path
from .views import MenuView, BookingView, MenuItemsView, SingleMenuItemView

urlpatterns = [
    path("menu/", MenuView.as_view()), 
    path("booking/", BookingView.as_view()),
    path("menu-items", MenuItemsView.as_view()),
    path("single-items", SingleMenuItemView.as_view()), 
       
]
