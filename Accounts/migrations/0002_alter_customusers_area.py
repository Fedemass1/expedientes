# Generated by Django 5.0.1 on 2024-01-28 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Exp', '0014_alter_pases_fecha_pase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Exp.areas'),
        ),
    ]