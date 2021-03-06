# Generated by Django 2.1.5 on 2019-02-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20190128_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='from_zip',
            field=models.CharField(max_length=5, verbose_name='From ZIP'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='other',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='quote',
            name='referral',
            field=models.CharField(blank=True, choices=[('ref_1', 'Friend'), ('ref_2', 'Social Media'), ('ref_3', 'Uhaul / MovingHelp'), ('ref_4', 'SML / Penske'), ('ref_5', 'ABF'), ('ref_6', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='quote',
            name='reff_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='quote',
            name='to_zip',
            field=models.CharField(max_length=5, verbose_name='To ZIP'),
        ),
    ]
