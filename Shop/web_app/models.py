from django.db import models

class Buyer(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

class Order(models.Model):
    PAPER_TYPE_CHOICES = [
        ('P1', 'Paper 1'),
        ('P2', 'Paper 2'),
        ('P3', 'Paper 3'),
        ('P4', 'Paper 4'),
        ('P5', 'Paper 5'),
        ('P6', 'Paper 6'),
        ('P7', 'Paper 7'),
        ('P8', 'Paper 8'),
        ('P9', 'Paper 9'),
        ('P10', 'Paper 10'),
    ]

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='orders')
    count = models.PositiveIntegerField()
    paper_type = models.CharField(max_length=4, choices=PAPER_TYPE_CHOICES)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.buyer.name} - {self.get_paper_type_display()}"
    
    
    # migret kon