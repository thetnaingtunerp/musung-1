# Generated by Django 5.0.6 on 2024-07-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_daily_report_hourcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_report',
            name='hourcount',
            field=models.PositiveIntegerField(default=11),
        ),
    ]
