# Generated by Django 3.2.23 on 2024-02-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0016_company_payment_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trialperiod',
            name='interested_in_buying',
            field=models.IntegerField(default=0),
        ),
    ]
