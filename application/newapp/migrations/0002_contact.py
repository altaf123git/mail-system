# Generated by Django 4.1.7 on 2023-03-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=10000)),
            ],
        ),
    ]