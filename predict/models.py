from django.db import models

# Create your models here.


class PatientInfo(models.Model):

    Age = models.IntegerField()
    Sex = models.CharField(max_length=30)
    Chest_Pain = models.CharField(max_length=30)
    Rest_BP = models.IntegerField()
    Cholestrol = models.IntegerField()
    Fast_BS = models.CharField(max_length=30)
    Rest_ECG = models.CharField(max_length=30)
    Max_Heart_Rate = models.IntegerField()
    Exercise = models.CharField(max_length=30)
    ExertoRest = models.FloatField()
    Slope = models.CharField(max_length=30)
    No_Major_Vessels = models.IntegerField()
    Thal = models.CharField(max_length=30)
    Heart_Disease = models.CharField(max_length=30)

    def __str__(self):
        return self.Heart_Disease
