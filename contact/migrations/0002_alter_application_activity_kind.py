# Generated by Django 4.0 on 2021-12-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='activity_kind',
            field=models.CharField(choices=[(None, 'Выберите вид вашей деятельности'), ('e', 'Работодатель'), ('t', 'Турист')], default='Выберите вид вашей деятельности', max_length=1),
        ),
    ]