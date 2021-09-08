# Generated by Django 3.2.7 on 2021-09-08 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCart',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('preparation_time', models.TimeField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('is_vegetarian', models.BooleanField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish', to='menu.menucart')),
            ],
        ),
    ]