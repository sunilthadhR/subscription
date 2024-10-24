# Generated by Django 4.2.16 on 2024-10-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spack', '0002_user_price_alter_user_pack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pack',
            field=models.CharField(blank=True, choices=[('1', 'basic'), ('2', 'premium'), ('3', 'basic-premium')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='price',
            field=models.IntegerField(blank=True, choices=[('1', '499'), ('2', '599'), ('3', '699')], max_length=50, null=True),
        ),
    ]
