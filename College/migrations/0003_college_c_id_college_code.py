# Generated by Django 4.1.5 on 2023-01-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0002_remove_college_c_id_remove_college_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='c_id',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='college',
            name='code',
            field=models.IntegerField(default=True),
        ),
    ]
