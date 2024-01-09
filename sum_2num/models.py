# myapp/models.py
from django.db import models

class Calculation(models.Model):
    operand1 = models.IntegerField()
    operand2 = models.IntegerField()
    result = models.IntegerField()
