# Generated by Django 5.0.1 on 2024-01-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SumResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField()),
                ('num2', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]
