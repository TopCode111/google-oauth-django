# Generated by Django 3.2.6 on 2021-10-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211022_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauth',
            name='manual_user',
            field=models.BooleanField(default=True),
        ),
    ]