# Generated by Django 4.2.4 on 2023-08-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangay',
            name='code',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
