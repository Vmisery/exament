# Generated by Django 4.1.2 on 2023-07-31 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('historia', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
                ('tecnica', models.CharField(max_length=30)),
            ],
        ),
    ]
