# Generated by Django 5.0 on 2024-01-09 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp', '0012_alter_expedientesprueba_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedientesprueba',
            name='nro_exp',
            field=models.IntegerField(),
        ),
    ]