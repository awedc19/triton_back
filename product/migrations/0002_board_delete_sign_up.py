# Generated by Django 4.2.6 on 2023-10-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('faist_name', models.CharField(max_length=50, null=True)),
                ('coporate_name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Sign_up',
        ),
    ]