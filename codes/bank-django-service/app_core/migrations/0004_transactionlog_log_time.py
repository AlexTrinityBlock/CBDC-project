# Generated by Django 3.2.16 on 2022-12-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0003_rename_withdraw_amount_transactionlog_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionlog',
            name='log_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
