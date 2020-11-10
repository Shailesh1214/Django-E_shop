from django.db import models
from django.core.validators import MinLengthValidator


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)


    def save(self):
        self.save()


    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False