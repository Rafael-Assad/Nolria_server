# Generated by Django 4.1.4 on 2023-01-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Illustrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('illustration', models.ImageField(blank=True, upload_to='illustrations')),
                ('hash', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('rows', models.IntegerField(default=1)),
                ('cols', models.IntegerField(default=1)),
                ('home_order', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('illustrated_at', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Illustrations',
            },
        ),
    ]
