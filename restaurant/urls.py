from django.urls import path, include
from .views import MenuView, BookingView, MenuItemsView, SingleMenuItemView, UserViewSet, BookingViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
routerr = routers.DefaultRouter() 
routerr.register(r'tables', BookingViewSet)

urlpatterns = [
    path("menu/", MenuView.as_view()), 
    path("booking/", BookingView.as_view()),
    path("menu-items/", MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('urls/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('bookings /', include(routerr.urls)),
    path('api-token-auth', obtain_auth_token),
]
