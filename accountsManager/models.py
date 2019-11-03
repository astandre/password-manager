from cryptographic_fields.fields import EncryptedCharField
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Account(models.Model):
    id_account = models.AutoField(primary_key=True, db_column='x0')
    site = models.CharField(max_length=300, blank=True, null=True, db_column='x1')
    user_name = models.CharField(max_length=300, blank=True, default="", db_column='x2')
    email = models.EmailField(blank=True, default="", db_column='x3')
    password = EncryptedCharField(max_length=20, db_column='x4')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        db_table = 't1'

    def __str__(self):
        if len(self.email) > 0:
            return f"{self.email}"
        else:
            return f"{self.user_name}"
