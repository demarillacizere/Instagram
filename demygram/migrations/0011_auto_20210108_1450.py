# Generated by Django 3.1.5 on 2021-01-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demygram', '0010_auto_20210108_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=240),
        ),
    ]
