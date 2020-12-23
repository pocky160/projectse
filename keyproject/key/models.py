from django.db import models

# Create your models here.

class Building(models.Model):
    IDBuilding = models.CharField(max_length=10, primary_key=True)
    NameBuilding = models.CharField(max_length=50)
    Floor = models.IntegerField()
    Room = models.IntegerField()

    def __str__(self):
        return self.NameBuilding

class Act(models.Model):
    IDAct = models.IntegerField(primary_key=True)
    NameAct = models.CharField(max_length=30)

    def __str__(self):
        return self.NameAct

class Booking(models.Model):
    IDBooking = models.AutoField(primary_key=True)
    NameBooking = models.CharField(max_length=30)
    DateBook = models.DateField()
    TimeStart = models.TimeField()
    TimeStop = models.TimeField()
    People = models.IntegerField()
    IDAct = models.ForeignKey(Act, on_delete=models.CASCADE)
    IDBuilding = models.ForeignKey(Building, on_delete=models.CASCADE)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.NameBooking