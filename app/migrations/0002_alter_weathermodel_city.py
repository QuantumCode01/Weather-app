# Generated by Django 4.1.4 on 2023-07-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weathermodel',
            name='city',
            field=models.CharField(default='Noida', max_length=50),
        ),
    ]
