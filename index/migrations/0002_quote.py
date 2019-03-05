# Generated by Django 2.1.5 on 2019-01-26 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_zip', models.IntegerField(max_length=5)),
                ('to_zip', models.IntegerField(max_length=5)),
                ('flights_from', models.CharField(max_length=10)),
                ('flights_to', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('from_property', models.CharField(max_length=10)),
                ('truck_size', models.IntegerField(help_text='ft', max_length=2)),
                ('insurance', models.BooleanField()),
                ('referral', models.TextField()),
                ('other', models.TextField()),
                ('reff_code', models.TextField(max_length=20)),
            ],
        ),
    ]