# Generated by Django 3.0.6 on 2020-05-25 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_company_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('DL', 'Delinquent'), ('SU', 'Signing Up'), ('SB', 'Subscribed')], default='SU', max_length=2),
        ),
    ]
