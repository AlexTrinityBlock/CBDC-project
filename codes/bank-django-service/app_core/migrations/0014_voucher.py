# Generated by Django 3.2.16 on 2022-11-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0013_administrator_access_control_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.IntegerField(max_length=100)),
                ('voucher_token', models.CharField(max_length=100)),
                ('is_used', models.IntegerField(max_length=10)),
            ],
        ),
    ]