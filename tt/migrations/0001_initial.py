# Generated by Django 4.0.5 on 2022-08-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='professor_subject',
            fields=[
                ('prof_subj_id', models.CharField(max_length=400, primary_key=True, serialize=False)),
                ('prof_name', models.CharField(max_length=400)),
                ('subj_name', models.CharField(max_length=400)),
                ('credits', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'professor_subject',
            },
        ),
    ]
