# Generated by Django 5.0.1 on 2024-01-09 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sum_2num', '0008_yourmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YourModel',
            new_name='Calculation',
        ),
        migrations.DeleteModel(
            name='AdditionResult',
        ),
        migrations.RenameField(
            model_name='calculation',
            old_name='num1',
            new_name='operand1',
        ),
        migrations.RenameField(
            model_name='calculation',
            old_name='num2',
            new_name='operand2',
        ),
    ]
