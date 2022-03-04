import os
import json
from classes import Character

# path for character files
save_path = 'characters/'

# Complete path for current character
def character_file(character_name):
    file_character_name = character_name.lower()
    character_file_name = file_character_name+".json"
    complete_file_name = os.path.join(save_path, character_file_name)
    return complete_file_name

# Creates JSON for new game character
def character_file_creation(character_name):
    character_file_name = character_file(character_name)
    character_dict = {"Name": character_name,
    "Current Health": Character.current_health,
    "Health": Character.health,
    "Agility": Character.agility,
    "Intelligent": Character.intelligent,
    "Strength": Character.intelligent,
    "Luck": Character.luck,
    "Defence": Character.defence,
    "Attack": Character.attack,
    "Experience": Character.experience}
    with open(character_file_name, mode='w') as f:
        json.dump(character_dict, f)

# Updates character stats from JSON file    
def update_character(character_name):
    character_file_name = character_file(character_name)
    character_data = open(character_file_name)
    character_json = json.load(character_data)
    character_details = Character(character_json["Name"],
        character_json["Current Health"],
        character_json["Health"],
        character_json["Agility"],
        character_json["Intelligent"],
        character_json["Strength"],
        character_json["Luck"],
        character_json["Defence"],
        character_json["Attack"],
        character_json["Experience"])
    character_data.close()
    return character_details

# Updates character stats to JSON file
def update_character_json(character_name, stat):
    character_file_name = character_file(character_name)
    character_json = open(character_file_name)
    character_details = json.load(character_json)
    character_json.close()
    if stat == Character.current_health:
        character_details["Current Health"] = Character.current_health
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    elif stat == Character.health:
        character_details["Health"] = Character.health
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    elif stat == Character.agility:
        character_details["Agility"] = Character.agility
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    elif stat == Character.intelligent:
        character_details["Intelligent"] = Character.intelligent
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    elif stat == Character.strength:
        character_details["Strength"] = Character.strength
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    elif stat == Character.luck:
        character_details["Luck"] = Character.luck
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    elif stat == Character.defence:
        character_details["Defence"] = Character.defence
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    elif stat == Character.attack:
        character_details["Attack"] = Character.attack
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    elif stat == Character.experience:
        character_details["Experience"] = Character.experience
        character_json = open(character_file_name, "w")
        json.dump(character_details, character_json)
        character_json.close()
    

