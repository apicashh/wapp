# Generated by Django 2.2.2 on 2019-06-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallerys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('typ', models.CharField(max_length=300)),
                ('direct_url', models.URLField()),
                ('site_name', models.CharField(max_length=300)),
                ('pics', models.ImageField(upload_to='')),
                ('thumbnail', models.URLField()),
            ],
        ),
    ]
