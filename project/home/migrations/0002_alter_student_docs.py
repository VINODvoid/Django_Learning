# Generated by Django 5.0.4 on 2024-05-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='docs',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
