# Generated by Django 3.1.1 on 2020-10-08 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20201008_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configfile',
            name='cid',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='config.configid'),
        ),
    ]
