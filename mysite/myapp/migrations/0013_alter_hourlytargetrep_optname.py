# Generated by Django 5.0.6 on 2024-06-06 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_hourlytargetrep_optname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourlytargetrep',
            name='optname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.operatortargetrep'),
        ),
    ]
