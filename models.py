# This is my table structure in the database.


from django.db import models


class Data(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    DOB = models.DateField()
