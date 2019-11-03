from django.db import models
from cryptographic_fields.fields import EncryptedCharField


# Create your models here.

class Account(models.Model):
    id_account = models.AutoField(primary_key=True, db_column='x0')
    site = models.CharField(max_length=300, blank=True, null=True, db_column='x1')
    user = models.CharField(max_length=300, blank=True, null=True, db_column='x2')
    email = models.EmailField(blank=True, null=True, db_column='x3')
    password = EncryptedCharField(max_length=12, db_column='x4')

    class Meta:
        default_related_name = 'accounts'
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        db_table = 't1'

    def __str__(self):
        if len(self.email) > 0:
            return f"{self.site}-{self.email}"
        else:
            return f"{self.site}-{self.user}"
