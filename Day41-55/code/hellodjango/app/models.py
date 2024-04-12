from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    corp = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'app_user'
