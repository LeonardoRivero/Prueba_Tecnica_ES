# Generated by Django 3.2.9 on 2021-11-07 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AnalogCameras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalsupport',
            name='camera',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AnalogCameras.camera'),
        ),
    ]