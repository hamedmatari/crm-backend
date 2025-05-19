from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuyerViewSet, OrderViewSet, LoginView , RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'buyer', BuyerViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),  # لاگین
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # رفرش توکن
    path('register/', RegisterView.as_view(), name='register'),
]

