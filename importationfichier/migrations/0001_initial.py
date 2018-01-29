# Generated by Django 2.0 on 2018-01-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='documents/')),
                ('importer', models.BooleanField(default=False)),
                ('date_importation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
