# Generated by Django 3.0.6 on 2020-06-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200531_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_setting',
            field=models.BooleanField(default=True),
        ),
    ]
