# Generated by Django 3.2.8 on 2021-11-11 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20211110_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reg_no',
            field=models.CharField(max_length=100, unique=True, verbose_name='Registration Number'),
        ),
    ]
