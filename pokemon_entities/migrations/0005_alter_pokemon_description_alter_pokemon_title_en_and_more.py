# Generated by Django 5.2 on 2025-04-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_alter_pokemon_description_alter_pokemon_title_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default=' ', verbose_name='Описание покемона'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=20, verbose_name='Имя покемона на английском языке'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default=2, max_length=20, verbose_name='Имя и произношение покемона на японском языке'),
            preserve_default=False,
        ),
    ]
