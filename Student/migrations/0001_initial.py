# Generated by Django 4.1.5 on 2023-01-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.IntegerField(max_length=20)),
                ('s_name', models.CharField(max_length=250)),
                ('s_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=200)),
            ],
        ),
    ]
