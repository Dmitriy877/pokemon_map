# Generated by Django 5.2 on 2025-04-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_remove_pokemon_next_evolution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя покемона на английском языке'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя и произношение покемона на японском языке'),
        ),
    ]
