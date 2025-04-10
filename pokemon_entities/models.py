from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="pokemons_photos", null=True)
    
    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
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
        return f"{self.latitude} {self.length}"
