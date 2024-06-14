from django.db import models

class StandardUser(models.Model):
    username = models.CharField(primary_key=True, max_length=150)
    password = models.CharField(max_length=250)
    emailid = models.EmailField(max_length=254)
    company = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)