# Generated by Django 4.0 on 2021-12-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetail',
            name='task_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
