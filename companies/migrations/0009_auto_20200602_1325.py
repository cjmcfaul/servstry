# Generated by Django 3.0.6 on 2020-06-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_company_default_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('SU', 'Signing Up'), ('SB', 'Subscribed'), ('DL', 'Delinquent'), ('EP', 'Expiring'), ('CL', 'Canceled'), ('EX', 'Example')], default='SU', max_length=2),
        ),
    ]
