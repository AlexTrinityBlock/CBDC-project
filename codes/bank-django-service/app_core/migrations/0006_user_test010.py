# Generated by Django 3.2.16 on 2022-11-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0005_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test010',
            field=models.CharField(max_length=100, null=True),
        ),
    ]