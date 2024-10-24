# Generated by Django 4.2.16 on 2024-10-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField()),
                ('smc', models.CharField(max_length=20, unique=True)),
                ('pack', models.CharField(choices=[('basic', 'basic'), ('premium', 'premium'), ('basic-premium', 'basic-premium')], max_length=20)),
            ],
        ),
    ]