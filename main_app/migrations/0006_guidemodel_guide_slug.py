# Generated by Django 4.1.1 on 2022-10-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_answer_to_guidemodel_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='guidemodel',
            name='guide_slug',
            field=models.CharField(default='default', max_length=50),
        ),
    ]