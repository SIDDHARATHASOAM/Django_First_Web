from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField( max_length=50)
    email =  models.CharField(max_length=150)
    phone =  models.CharField( max_length=12)
    desc =  models.TextField()
    date=   models.DateField() 

    def __str__(self):
        return self.name    # this function help me in data-base and change objects number t name of user as per record
        