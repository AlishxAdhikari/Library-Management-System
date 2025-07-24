from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    author = models.CharField(max_length=100, default="Unknown Author")
    received_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"