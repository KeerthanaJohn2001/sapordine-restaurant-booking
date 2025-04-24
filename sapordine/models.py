from django.db import models

# Create your models here.
class SliderImage(models.Model):
    image=models.ImageField(null=True)
    title=models.CharField(max_length=250,null=True)
    class Meta:
        db_table="sliderimage"

class Menu(models.Model):
    image=models.ImageField(upload_to='static/images')
    name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    class Meta:
        db_table="FoodMenu"

class TableReservation(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    no_of_people=models.IntegerField()
    message=models.CharField(max_length=250)
    class Meta:
        db_table="TableReservation"
class UserSignup(models.Model):
    name=models.CharField(max_length=150)
    phone_number=models.IntegerField()
    email=models.EmailField(max_length=55,unique=True)
    password=models.CharField(max_length=150)
    class Meta:
        db_table="UserSignup"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"  




   