# Generated by Django 3.2.16 on 2022-11-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0007_auto_20221120_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='bankCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('encrypt_coin_seq', models.IntegerField()),
                ('sign_encrypt_coin_seq', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.IntegerField()),
                ('coin_seq', models.IntegerField()),
                ('sign_coin_seq', models.IntegerField()),
            ],
        ),
    ]
