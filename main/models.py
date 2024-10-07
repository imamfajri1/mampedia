import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AtributEntery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    time = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()