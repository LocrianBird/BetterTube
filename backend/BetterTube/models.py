from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):

    def create_user(self, user_id, token_uri=None, client_id=None, client_secret=None, first_name=None, last_name=None, email=None, access_token=None, refresh_token=None, id_token=None, avatar_url=None):
        user = User()
        user.user_id = user_id
        user.access_token = access_token
        user.id_token = id_token
        user.refresh_token = refresh_token
        user.avatar_url = avatar_url
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.token_uri = token_uri
        user.client_id = client_id
        user.client_secret = client_secret
        user.save(using=self._db)
        return user

    def create_super_user(self):
        pass


class User(AbstractUser):
    user_id = models.TextField(unique=True, primary_key=True)
    access_token = models.TextField(null=True)
    id_token = models.TextField(null=True)
    refresh_token = models.TextField(null=True)
    avatar_url = models.TextField(null=True)
    token_uri = models.TextField(null=True)
    client_id = models.TextField(null=True)
    client_secret = models.TextField(null=True)
    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []
