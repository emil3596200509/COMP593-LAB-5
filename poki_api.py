"""
Library for interacting with the PokeAPI.
https://pokeapi.co/
"""
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    poke_info = get_pokemon_info("Rockruff")
    if poke_info:
        print(f"Pokemon Name: {poke_info['name']}")
        print(f"Abilities: {[ability['ability']['name'] for ability in poke_info['abilities']]}")
    else:
        print("Failed to fetch Pokémon information.")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokémon from the PokeAPI.

    Args:
        pokemon_name (str): Pokémon name (or Pokédex number)

    Returns:
        dict: Dictionary of Pokémon information, if successful. Otherwise None.
    """
    # Clean the Pokémon name parameter
    pokemon_name = str(pokemon_name).strip().lower()

    # Build a clean URL and use it to send a GET request
    url = f"{POKE_API_URL}{pokemon_name}"
    print(f"Fetching information for {pokemon_name}...", end='')
    response = requests.get(url)

    # Check if the GET request was successful
    if response.status_code == 200:
        print('success')
        return response.json()  # Convert the JSON-formatted message body text to a dictionary and return it
    else:
        print('failure')
        print(f"Response code: {response.status_code} ({response.reason})")
        return None

if _name_ == '_main_':
    main()