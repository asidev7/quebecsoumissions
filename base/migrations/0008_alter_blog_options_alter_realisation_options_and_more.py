# Generated by Django 5.0.6 on 2024-08-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_blog_contenu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='realisation',
            options={'verbose_name': '', 'verbose_name_plural': 'Fonctionnalités'},
        ),
        migrations.AlterModelOptions(
            name='type_soumission',
            options={'verbose_name': 'Type de soumission', 'verbose_name_plural': 'Type de soumission'},
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
