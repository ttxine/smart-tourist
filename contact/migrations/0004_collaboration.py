# Generated by Django 4.0 on 2021-12-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_employerapplication_touristapplication_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название сотрудничающей организации')),
                ('short_description', models.TextField(max_length=500, verbose_name='Краткое описание организации')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Ссылка на подробности организации')),
            ],
            options={
                'verbose_name': 'Сотрудничающая организация',
                'verbose_name_plural': 'Сотрудничающие организации',
            },
        ),
    ]
