# Generated by Django 4.2.5 on 2023-10-03 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_producto_imagen_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_url',
            field=models.URLField(max_length=4000),
        ),
    ]