# Generated by Django 5.0.6 on 2024-06-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='PAYMENT',
            field=models.CharField(choices=[('Cash on delivery', 'Cash on delivery'), ('Esewa', 'Esewa')], max_length=50, null=True),
        ),
    ]
