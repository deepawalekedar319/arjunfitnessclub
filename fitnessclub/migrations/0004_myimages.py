# Generated by Django 4.0.3 on 2022-03-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessclub', '0003_moreimages_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=126)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]