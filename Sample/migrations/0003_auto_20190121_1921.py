# Generated by Django 2.1.5 on 2019-01-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sample', '0002_auto_20190121_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentform',
            name='sec',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentform',
            name='sem',
            field=models.IntegerField(),
        ),
    ]