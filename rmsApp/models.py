from django.db import models

# Create your models here.
class ReportDetails(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=128)
    runReport = models.CharField(max_length=30)
    supportedCountry = models.CharField(max_length=30)
    editionNumber = models.CharField(max_length=30)
    module = models.CharField(max_length=30)