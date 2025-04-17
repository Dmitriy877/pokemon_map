from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title = models.CharField(max_length=20, verbose_name="Покемон")
    title_en = models.CharField(max_length=20, blank=True, verbose_name="Имя покемона на английском языке")
    title_jp = models.CharField(max_length=20, blank=True, verbose_name="Имя и произношение покемона на японском языке")
    picture = models.ImageField(upload_to="pokemons_photos", null=True, verbose_name="Изображени покемона")
    description = models.TextField(blank=True, verbose_name="Описание покемона")
    previous_evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="next_evolutions",
        verbose_name="Прошлая эволюция покемона"
    )
    
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="pokemon_entities", verbose_name="Покемон")
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(null=True, verbose_name="Время появления покемона")
    disappeared_at = models.DateTimeField(null=True, verbose_name="Время ухода покемона")
    level = models.IntegerField(null=True, blank=True, verbose_name="Уровень покемона")
    health = models.IntegerField(null=True, blank=True, verbose_name="Здоровье покемона")
    attack = models.IntegerField(null=True, blank=True, verbose_name="Атака покемона")
    defend = models.IntegerField(null=True, blank=True, verbose_name="Защита покемона")
    stamina = models.IntegerField(null=True, blank=True, verbose_name="Выносливость покемона")
    
    def __str__(self):
        return f"{self.lat} {self.lon}"
