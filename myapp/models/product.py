from django.db import models
from django.utils import timezone


class Product(models.Model):
    class FormEnum(models.TextChoices):
        RAW = 'raw', 'Raw'
        DISPATCH = 'dispatch', 'Dispatch'
    challan_no = models.CharField(max_length=100, default="-")
    company = models.CharField(max_length=255, default="-")
    date = models.DateField()
    design = models.CharField(max_length=255, default="-")
    type = models.CharField(max_length=255, default="-")
    size = models.CharField(max_length=100, default="-")
    color = models.CharField(max_length=100, default="-")
    quantity = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True, default="-")
    shuttle_or_mat = models.CharField(max_length=100, default="-")
    receiving = models.CharField(max_length=100, default="-")
    form_enum = models.CharField(
        max_length=50,
        choices=FormEnum.choices,
        default=FormEnum.RAW,
    )
    def __str__(self):
        return f"{self.challan_no} - {self.company}"

