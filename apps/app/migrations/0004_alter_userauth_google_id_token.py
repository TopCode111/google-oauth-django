# Generated by Django 3.2.6 on 2021-10-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userauth_manual_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauth',
            name='google_id_token',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
