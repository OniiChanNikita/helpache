# Generated by Django 4.1.1 on 2022-10-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_guidemodel_guide_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidemodel',
            name='categories',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='guidemodel',
            name='title_guide',
            field=models.CharField(max_length=500),
        ),
    ]