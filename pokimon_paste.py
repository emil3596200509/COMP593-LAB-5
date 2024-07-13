"""
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage: python pokemon_paste.py poke_name

"""
import sys
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(poke_name)
    if poke_info is not None:
        paste_title, paste_body = get_paste_data(poke_info)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M', listed=False)
        if paste_url:
            print(f"Paste created successfully! URL: {paste_url}")
        else:
            print("Failed to create paste.")
    else:
        print("Failed to fetch Pokémon information.")

def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        print('Error: Pokemon name not provided.')
        sys.exit('Script execution aborted')

def get_paste_data(pokemon_info):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.

    Args:
        pokemon_info (dict): Dictionary of Pokemon information

    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    # Build the paste title
    pokemon_name = pokemon_info['name'].capitalize()
    title = f"{pokemon_name}'s Abilities"

    # Build the paste body text
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    body_text = "\n".join(f"- {ability}" for ability in abilities)
    
    return title, body_text

if _name_ == '_main_':
    main()