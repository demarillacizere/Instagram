# Generated by Django 3.1.5 on 2021-01-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demygram', '0012_remove_comment_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=240),
        ),
    ]
