# Generated by Django 4.1.2 on 2022-11-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_tel_rasmlari_rasm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tel_rasmlari',
            name='rasm',
            field=models.ImageField(upload_to='tel_rasmlari '),
        ),
    ]
