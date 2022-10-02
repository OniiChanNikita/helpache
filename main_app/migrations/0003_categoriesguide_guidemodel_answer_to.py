# Generated by Django 4.1.1 on 2022-10-02 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_guidemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='guidemodel',
            name='answer_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.categoriesguide'),
        ),
    ]
