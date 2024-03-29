# Generated by Django 3.0.8 on 2023-03-20 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdie_app', '0012_auto_20210901_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birdie',
            name='course',
            field=models.CharField(blank=True, choices=[('Broadmoor', 'Broadmoor'), ('Camas Meadows', 'Camas Meadows'), ('Colwood', 'Colwood'), ('Heron Lakes Great Blue', 'Heron Lakes Great Blue'), ('Heron Lakes Greenback', 'Heron Lakes Greenback'), ('Lewis River', 'Lewis River'), ('Mint Valley', 'Mint Valley'), ('Riverside Golf Club', 'Riverside Golf Club'), ('Tri Mountain', 'Tri Mountain'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='birdie',
            name='player',
            field=models.CharField(blank=True, choices=[('Bryan', 'Bryan'), ('David', 'David'), ('Greg', 'Greg'), ('Kara', 'Kara'), ('Steve', 'Steve')], max_length=10, null=True),
        ),
    ]
