# Generated by Django 3.1.13 on 2024-01-31 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdie_app', '0013_auto_20230320_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birdie',
            name='course',
            field=models.CharField(blank=True, choices=[('Camas Meadows', 'Camas Meadows'), ('Colwood', 'Colwood'), ('Heron Lakes Great Blue', 'Heron Lakes Great Blue'), ('Heron Lakes Greenback', 'Heron Lakes Greenback'), ('Lewis River', 'Lewis River'), ('Mint Valley', 'Mint Valley'), ('Riverside Golf Club', 'Riverside Golf Club'), ('Tri Mountain', 'Tri Mountain'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
