# Generated by Django 2.2.7 on 2021-03-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yunnote', '0003_auto_20210322_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='分组名称'),
        ),
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(max_length=20, verbose_name='笔记名称'),
        ),
    ]
