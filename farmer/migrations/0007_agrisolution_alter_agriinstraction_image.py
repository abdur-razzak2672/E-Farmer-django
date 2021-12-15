# Generated by Django 4.0 on 2021-12-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_rename_instractions_agriinstraction'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgriSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='farmer/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='agriinstraction',
            name='image',
            field=models.ImageField(upload_to='farmer/images'),
        ),
    ]
