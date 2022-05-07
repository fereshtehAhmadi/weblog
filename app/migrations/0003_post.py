# Generated by Django 3.2 on 2022-05-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_users_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('create', models.DateTimeField(auto_now=True)),
                ('modify', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
