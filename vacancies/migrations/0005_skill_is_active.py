# Generated by Django 4.1.7 on 2023-03-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_alter_skill_options_alter_vacancy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
