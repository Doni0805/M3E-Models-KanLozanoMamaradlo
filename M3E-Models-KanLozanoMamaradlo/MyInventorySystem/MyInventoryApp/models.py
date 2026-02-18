from django.db import models
from django.utils import timezone

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)

    def getName(self):
        return self.name

    def __str__(self):
        return f"{str(self.pk)}: {self.name} - {self.city}, {self.country} created at: {self.created_at}" 
    

class WaterBottle(models.Model):

    # Makes sure there are no duplicates
    sku = models.CharField(max_length=20, unique=True)

    brand = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100)
    mouthSize = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    
    supplierName = models.ForeignKey(   # To allow supplier to supply multiple SKUs
        Supplier,                       # points to the model Supplier
        on_delete=models.PROTECT,       # protects the model from being deleted if there are bottles within it
    )
    currentQuantity = models.IntegerField()
    
    def __str__(self):
        return (f"{self.sku}: {self.brand}, {self.mouthSize}, {self.size}, {self.color}, supplied by"
                f"{self.supplierName}, {self.cost}: {self.currentQuantity}")
        
