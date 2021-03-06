# Generated by Django 2.2.6 on 2019-11-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, db_column='x3', default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_name',
            field=models.CharField(blank=True, db_column='x2', default='', max_length=300),
        ),
    ]
