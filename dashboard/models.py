from pickle import TRUE
from sre_parse import CATEGORIES
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('stationary','stationary'),
    ('Electronics','Electronics'),
    ('Food','Food')
)


class product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity =models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'