from django.db import models
from django.contrib.auth import get_user_model

class PromoCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount = models.FloatField(default=60.0)  # 60% discount
    usage_count = models.IntegerField(default=0)

    def __str__(self):
        return self.code
