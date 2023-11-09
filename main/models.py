import uuid
from django.db import models

class CarPass(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=48)
    model = models.CharField(max_length=48)
    plate_number = models.CharField(max_length=24)
    owners_name = models.CharField(max_length=96)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

