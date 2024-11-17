# Generated by Django 5.1.3 on 2024-11-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=128)),
                ('runReport', models.CharField(max_length=30)),
                ('supportedCountry', models.CharField(max_length=30)),
                ('editionNumber', models.CharField(max_length=30)),
                ('module', models.CharField(max_length=30)),
            ],
        ),
    ]
