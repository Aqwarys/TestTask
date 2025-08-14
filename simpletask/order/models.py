from django.db import models
from user.models import User

class Order(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Order Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='User')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
