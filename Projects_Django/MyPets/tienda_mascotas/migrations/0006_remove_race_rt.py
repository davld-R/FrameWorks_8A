# Generated by Django 3.2.7 on 2021-10-09 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_mascotas', '0005_auto_20211009_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='rt',
        ),
    ]
