from django.db import models

# Create your models here.

class churn_prediction(models.Model):
    CreditScore = models.FloatField()
    Gender = models.FloatField()
    Age = models.FloatField()
    Tenure = models.FloatField()
    Balance = models.FloatField()
    NumOfProducts = models.FloatField()
    HasCrCard = models.FloatField()
    IsActiveMember = models.FloatField()
    EstimatedSalary = models.FloatField()
    Exited = models.FloatField()
