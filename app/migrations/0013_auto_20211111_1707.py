# Generated by Django 3.2.8 on 2021-11-11 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20211111_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='maindomain', to='app.domain'),
        ),
        migrations.AlterField(
            model_name='results',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
