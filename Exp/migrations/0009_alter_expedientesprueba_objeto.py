# Generated by Django 5.0 on 2024-01-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp', '0008_alter_expedientesprueba_objeto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedientesprueba',
            name='objeto',
            field=models.TextField(max_length=500),
        ),
    ]