# Generated by Django 5.0.6 on 2024-08-07 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='nom',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
