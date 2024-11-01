# Generated by Django 4.2.16 on 2024-10-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='price',
            field=models.CharField(blank=True, choices=[('499', '499'), ('599', '599'), ('699', 'basic-premium')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pack',
            field=models.CharField(blank=True, choices=[('basic', 'basic'), ('premium', 'premium'), ('basic-premium', 'basic-premium')], max_length=20, null=True),
        ),
    ]
