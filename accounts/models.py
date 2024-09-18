from django.db import models
from django.contrib.auth.models import AbstractUser

# create user model here
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_engineer = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    # USERNAME_FIELD = 'username' # le user sera identifié par son emailm
    # REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username
# Create your models here.
