# Generated by Django 5.0.6 on 2024-05-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='logo')),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('numero_telephone', models.CharField(max_length=20)),
            ],
        ),
    ]
