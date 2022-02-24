from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    

class Shop(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.name
    
class Visit(models.Model):
    date = models.DateTimeField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self) -> str:
        return self.id
    
