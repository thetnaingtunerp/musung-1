# Generated by Django 5.0.6 on 2024-06-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_operatortargetrep_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourlytargetrep',
            name='optname',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.operatortargetrep'),
        ),
    ]
