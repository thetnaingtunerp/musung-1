# Generated by Django 5.0.6 on 2024-06-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_operator_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='burmese',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
