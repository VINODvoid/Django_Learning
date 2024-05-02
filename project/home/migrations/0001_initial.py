# Generated by Django 5.0.4 on 2024-05-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('docs', models.FileField(upload_to='')),
                ('standard', models.CharField(max_length=10)),
            ],
        ),
    ]
