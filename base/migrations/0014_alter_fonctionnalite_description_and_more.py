# Generated by Django 5.0.6 on 2024-08-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_soumission_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fonctionnalite',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='fonctionnalite',
            name='nom',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
