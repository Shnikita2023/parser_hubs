# Generated by Django 5.0.3 on 2024-03-08 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, unique=True, verbose_name='Заголовок')),
                ('hub_link', models.CharField(db_index=True, unique=True, verbose_name='Ссылка на хаб')),
            ],
            options={
                'verbose_name': 'Хаб',
                'verbose_name_plural': 'Хабы',
                'db_table': 'hub',
            },
        ),
    ]
