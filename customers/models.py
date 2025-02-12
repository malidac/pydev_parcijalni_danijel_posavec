from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    vatid = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
    
        super().save(*args, **kwargs)

    @classmethod
    def from_tuple(cls, data):
        
        return cls(id=data[0], name=data[1], description=data[2], price=data[3])

    @classmethod
    def get_all(cls):
       
        return cls.objects.all()
