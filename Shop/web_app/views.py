from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Buyer, Order
from .serializers import BuyerSerializer, OrderSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]



class LoginView(TokenObtainPairView):
    
    pass



class BuyerViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'phone_number']
    search_fields = ['name', 'phone_number']
    
    
    
class DeleteBuyerView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        try:
            phone_number = kwargs['phone_number']
            buyer = Buyer.objects.get(phone_number=phone_number)
            buyer.delete()
            return Response({"message": "Buyer deleted successfully"}, status=204)
        except Buyer.DoesNotExist:
            return Response({"error": "Buyer not found"}, status=404)
        
        
            
    
    
class OrderViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    



class DeleteOrderView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        try:
            order_id = kwargs['order_id']
            order = Order.objects.get(id=order_id)
            order.delete()
            return Response({"message": "Order deleted successfully"}, status=204)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)