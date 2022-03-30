# Generated by Django 4.0.3 on 2022-03-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('day', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateField(blank=True, max_length=100, null=True)),
                ('doc', models.CharField(blank=True, max_length=100, null=True)),
                ('textarea_message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]