# Generated by Django 4.1.7 on 2023-03-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std', '0003_student_pan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pan',
            field=models.FileField(default='abc', upload_to='static', verbose_name='pan'),
        ),
    ]
