# Generated by Django 5.0.6 on 2024-06-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Saved', 'Saved')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
