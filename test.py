# Completely for testing

import os
import json

from classes import Character 

save_path = 'characters/'
character_name = "Tim"
Character.attack = 100

def character_file(character_name):
    file_character_name = character_name.lower()
    character_file_name = file_character_name+".json"
    complete_name = os.path.join(save_path, character_file_name)
    return complete_name

def update_character_json(character_name):
    character_file_name = character_file(character_name)
    character_json = open(character_file_name)
    character_details = json.load(character_json)
    character_json.close()
    print(character_details["Attack"])
    character_details["Attack"] = Character.attack
    character_json = open(character_file_name, "w")
    json.dump(character_details, character_json)
    character_json.close()


def main():
    character_file(character_name)
    update_character_json(character_name)

main()