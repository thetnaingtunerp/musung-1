# Generated by Django 4.1.7 on 2024-08-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_daily_report_workinghr'),
    ]

    operations = [
        migrations.CreateModel(
            name='ferry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ferryname', models.CharField(max_length=255)),
                ('lic_number', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
