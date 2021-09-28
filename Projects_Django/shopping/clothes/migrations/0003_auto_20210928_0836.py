# Generated by Django 3.2.7 on 2021-09-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_marca_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='marca',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]
