from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuyerViewSet, OrderViewSet, LoginView, RegisterView, DeleteBuyerView , DeleteOrderView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'buyer', BuyerViewSet)   # ایجاد مسیرهای CRUD برای خریدار
router.register(r'order', OrderViewSet)   # ایجاد مسیرهای CRUD برای سفارش

urlpatterns = [
    path('', include(router.urls)),  # شامل تمام مسیرهای ساخته‌شده با router
    path('login/', LoginView.as_view(), name='token_obtain_pair'),  # لاگین JWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # رفرش توکن
    path('register/', RegisterView.as_view(), name='register'),  # ثبت‌نام کاربر
    path('delete/buyer/<str:phone_number>/', DeleteBuyerView.as_view(), name='delete-buyer-by-phone'),  # حذف با شماره تلفن
    path('delete/order/id/', DeleteOrderView.as_view(), name='DeleteOrder'),
]