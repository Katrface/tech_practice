# Generated by Django 2.2.17 on 2020-11-13 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название статьи')),
                ('link', models.CharField(max_length=100, verbose_name='ссылка на статью')),
                ('photo_link', models.CharField(max_length=100, verbose_name='ссылка на фото')),
            ],
        ),
        migrations.CreateModel(
            name='HeadArticleCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.ArticleCard')),
            ],
        ),
    ]
