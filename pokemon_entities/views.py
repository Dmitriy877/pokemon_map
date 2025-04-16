import folium


from django.http import HttpResponseNotFound
from django.shortcuts import render

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
    pokemons_entity = PokemonEntity.objects.all()
    print(pokemons_entity)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entity:
        picture_url = request.build_absolute_uri(pokemon_entity.pokemon.picture.url)
        add_pokemon(
            folium_map, pokemon_entity.lat,
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

    requested_pokemon = {
        "pokemon_id": pokemon.id,
        "title_ru": pokemon.title,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "img_url": request.build_absolute_uri(pokemon.picture.url),
        "entities": [],
        "previous_evolution": {},
        "next_evolution": {}

    }
    
    for pokemon_entity in pokemon.pokemon_entities.all():
        requested_pokemon["entities"].append({
            "lat": pokemon_entity.lat,
            "lon": pokemon_entity.lon
            })
        
    if pokemon.previous_evolution:
        requested_pokemon["previous_evolution"] = {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": request.build_absolute_uri(pokemon.previous_evolution.picture.url)
        }
    
    if pokemon.next_evolution:
        requested_pokemon["next_evolution"] = {
            "title_ru": pokemon.next_evolution.title,
            "pokemon_id": pokemon.next_evolution.id,
            "img_url": request.build_absolute_uri(pokemon.next_evolution.picture.url)
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemon['entities']:
        add_pokemon(
            folium_map,
            pokemon_entity['lat'],
            pokemon_entity['lon'],
            requested_pokemon['img_url']
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': requested_pokemon
    })
