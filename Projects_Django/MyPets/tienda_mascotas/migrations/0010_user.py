# Generated by Django 3.2.7 on 2021-10-09 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_mascotas', '0009_identification_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('number_id', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
                ('id_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.city')),
                ('id_identification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_mascotas.identification_type')),
            ],
        ),
    ]