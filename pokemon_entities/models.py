from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20, blank=True)
    title_jp = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to="pokemons_photos", null=True)
    description = models.TextField(blank=True)
    previous_evolution = models.ForeignKey("Pokemon", on_delete=models.SET_NULL, null=True, blank=True, related_name="past_evolution")
    next_evolution = models.ForeignKey("Pokemon", on_delete=models.SET_NULL, null=True, blank=True, related_name="future_evolution")
    
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="pokemon_entities")
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defend = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.lat} {self.lon}"
