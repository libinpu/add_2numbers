# Generated by Django 5.0.1 on 2024-01-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sum_2num', '0003_additionresult_delete_calculation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.FloatField()),
                ('num2', models.FloatField()),
                ('result', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='AdditionResult',
        ),
    ]
