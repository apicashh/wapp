# Generated by Django 2.2.2 on 2019-07-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wapp', '0003_fhg_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fhg_models',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
