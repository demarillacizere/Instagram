# Generated by Django 3.1.5 on 2021-01-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demygram', '0009_auto_20210104_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
