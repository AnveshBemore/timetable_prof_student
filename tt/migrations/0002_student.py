# Generated by Django 4.0.5 on 2022-08-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('std_id', models.IntegerField(primary_key=True, serialize=False)),
                ('std_name', models.CharField(max_length=500)),
                ('course1', models.CharField(max_length=500)),
                ('course2', models.CharField(max_length=500)),
                ('course3', models.CharField(max_length=500)),
                ('course4', models.CharField(max_length=500)),
                ('course5', models.CharField(max_length=500)),
                ('course6', models.CharField(max_length=500)),
                ('course7', models.CharField(max_length=500)),
                ('course8', models.CharField(max_length=500)),
            ],
        ),
    ]
