# Generated by Django 5.0 on 2023-12-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geografia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='alcalde',
            field=models.CharField(max_length=100),
        ),
    ]
