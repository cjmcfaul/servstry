# Generated by Django 3.0.6 on 2020-05-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20200523_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='customer_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]