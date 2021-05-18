# Generated by Django 3.2 on 2021-05-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('project_description', models.TextField(max_length=500)),
                ('github_link', models.CharField(blank=True, max_length=100)),
                ('app_link', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
