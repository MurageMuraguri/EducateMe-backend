# Generated by Django 2.2.19 on 2021-04-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.CharField(max_length=24, primary_key=True, serialize=False),
        ),
    ]