# models.py
from django.db import models

class Loom(models.Model):
    date = models.DateField()
    loomNo = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    design = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default="-")
    warp = models.CharField(max_length=100)
    warpColor = models.CharField(max_length=100)
    weft = models.CharField(max_length=100)
    weftColor = models.CharField(max_length=100)
    widthInch = models.IntegerField()
    lengthMeter = models.IntegerField()
    threadCount = models.IntegerField()
    reed = models.CharField(max_length=100)
    bOrM = models.CharField(max_length=50)
    dentThread = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.loomNo} - {self.company}"
