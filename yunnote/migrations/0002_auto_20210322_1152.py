# Generated by Django 2.2.7 on 2021-03-22 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yunnote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='group_id',
            field=models.IntegerField(verbose_name='分组ID'),
        ),
    ]
