# Generated by Django 5.0.6 on 2024-08-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_blog_options_alter_realisation_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='nom_entreprise',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
