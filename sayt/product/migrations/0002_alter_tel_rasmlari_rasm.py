# Generated by Django 4.0 on 2022-10-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tel_rasmlari',
            name='rasm',
            field=models.ImageField(upload_to='tel_rasmlari'),
        ),
    ]
