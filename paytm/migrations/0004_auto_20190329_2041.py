# Generated by Django 2.1.7 on 2019-03-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0003_remove_paytm_history_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytm_history',
            name='BANKTXNID',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='BANK TXN ID'),
        ),
    ]
