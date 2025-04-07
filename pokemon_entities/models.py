from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="pokemons_photos", null=True)

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f"{self.latitude} {self.length}"
