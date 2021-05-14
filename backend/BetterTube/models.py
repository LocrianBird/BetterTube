from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):

    def create_user(self, client_id, token=None, refresh_token=None, token_uri=None, client_secret=None, avatar_url=None):
        user = User()
        user.client_id = client_id
        user.token = token
        user.refresh_token = refresh_token
        user.token_uri = token_uri
        user.client_secret = client_secret
        user.avatar_url = avatar_url
        user.save(using=self._db)
        return user


    def create_super_user(self):
        pass


class User(AbstractUser):
    client_id = models.TextField(unique=True, primary_key=True)
    token = models.TextField(null=True)
    refresh_token = models.TextField(null=True)
    token_uri = models.TextField(null=True)
    client_secret = models.TextField(null=True)
    avatar_url = models.TextField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'client_id'
    REQUIRED_FIELDS = []
