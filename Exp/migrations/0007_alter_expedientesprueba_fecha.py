# Generated by Django 5.0 on 2024-01-08 21:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp', '0006_alter_expedientesprueba_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedientesprueba',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]