# Generated by Django 5.0.6 on 2024-07-15 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_operator_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_report',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
