# Generated by Django 4.1.6 on 2023-04-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_auto_20230201_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
