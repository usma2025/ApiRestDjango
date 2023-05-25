from django.db import models
from django.db.models import ForeignKey
import hashlib

class Login(models.Model):
    cedulaCiudadania = models.CharField(max_length=20, primary_key=True)
    user = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)

    def set_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest()

class Register(models.Model):
    cedulaCiudadania = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.TextField()
    lastName = models.TextField()
    birthday = models.DateField()
    gender = models.TextField()

class Posts(models.Model):
    user = models.ForeignKey(Login,to_field='user', on_delete=models.CASCADE)
    description = models.TextField()
    images = models.TextField()
    date = models.DateField()

# Create your models here.
