# Generated by Django 3.0.7 on 2022-01-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0006_event_reg_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_reg',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]