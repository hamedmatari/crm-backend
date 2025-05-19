from django.db import models

class Buyer(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

class Order(models.Model):
    
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='orders')
    count = models.PositiveIntegerField()
    paper_type = models.CharField(max_length=50)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.buyer.name} - {self.paper_type}"
