from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(default=datetime.now)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    