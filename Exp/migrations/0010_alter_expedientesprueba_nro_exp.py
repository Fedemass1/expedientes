# Generated by Django 5.0 on 2024-01-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp', '0009_alter_expedientesprueba_objeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedientesprueba',
            name='nro_exp',
            field=models.IntegerField(unique=True),
        ),
    ]