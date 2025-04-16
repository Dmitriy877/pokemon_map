import folium
import json


from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone

from pokemon_entities.models import Pokemon
from pokemon_entities.models import PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    pokemons = Pokemon.objects.all()
    alive_pokemons = PokemonEntity.objects.filter(
        appeared_at__lte=timezone.localtime(),
        disappeared_at__gte=timezone.localtime()
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in alive_pokemons:
        picture_url = request.build_absolute_uri(pokemon_entity.pokemon.picture.url)
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            picture_url
        )

    pokemons_on_page = []

    for pokemon in pokemons:

        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.picture.url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    print(pokemon)
    requested_pokemon = PokemonEntity.objects.filter(pokemon=pokemon)
    print(requested_pokemon)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemon:
        picture_url = request.build_absolute_uri(pokemon_entity.pokemon.picture.url)
        print(picture_url)
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            picture_url
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
