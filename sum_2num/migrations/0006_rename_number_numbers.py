# Generated by Django 5.0.1 on 2024-01-09 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sum_2num', '0005_number_delete_calculation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Number',
            new_name='Numbers',
        ),
    ]
