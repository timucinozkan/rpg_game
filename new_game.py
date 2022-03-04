from xml.dom.minidom import Element
from character_details import character_file_creation, update_character, update_character_json
from classes import Character

# Func for getting character name
def player_name():
    print("Hmmm, nedense daha once tanistik saniyordum?\nMadem oyle kolay bir soruyla baslayalim mi?\n")
    while True:
        character_name = input("Sana nasil hitap etmemi istersin?\n\n>>>")
        try:
            _ = int(character_name)
        except:
            if len(character_name) > 0:
                character_name_list = list(character_name)
                character_name_list[0] = character_name_list[0].upper()
                character_name = "".join([str(elem) for elem in character_name_list])
                break
            else:
                print("Seni duyamadim ya da bana adini soylemedin.")
        else:
            print("Macera arkadasima duzgun sekilde seslenmeyi tercih ederim. Tekrar dene, hadi!")
    character_file_creation(character_name)
    return character_name

# Func for first attribute increase
def player_build_1(character_name):
    print("\n\nTanistigima memnun oldum {}!".format(character_name))
    print("Peki {}, biraz daha yakinlasmaya ne dersin? Sence bu seceneklerden hangisi daha onemli?".format(character_name))
    character_details = update_character(character_name)
    while True:
        try:
            selection_range = range(1,7)
            attribute_selection = int(input('1 - Hiz\n2 - Guc\n3 - Bilgi\n4 - Savunma\n5 - Saldiri\n6 - Tecrube\n\n\n>>>'))
            if attribute_selection in selection_range:
                break
            else:
                print("6 basit secenek, bence yapabilirsin! Senin secimin olan {} bunlardan biri degil ne yazik ki.".format(attribute_selection))
        except ValueError:
            print("Bu kadar zor degil. Odaklanmaya calis!\nSana verdigim seceneklerden bir tanesini sec.")
    if attribute_selection == 1:
        print("Hmmm, cevik olmak cogunlukla hayatta kalmani saglar, degil mi? Peki sence ceviklik bu dunyada isine yarayacak mi?\n")
        Character.agility = Character.agility + 3
        update_character_json(character_name,Character.agility)
        print("+3 ceviklik kazandin.")
    elif attribute_selection == 2:
        print("Seni o kadar iyi anliyorum ki. Bir balta darbesiyle halledilemeyecek hic bir sey yoktur. Duygusal iliskileri saymazsak...\n")
        Character.strength = Character.strength + 3
        update_character_json(character_name,Character.strength)
        print("+3 guc kazandin.")
    elif attribute_selection ==  3:
        print("Yillardir tartisilan 'Cok okuyan mi yoksa cok gezen mi?' sorusunun cevabini bulmussun anlasilan.\n")
        Character.intelligent = Character.intelligent + 3
        update_character_json(character_name,Character.intelligent)
        print("+3 bilgi kazandin.")
    elif attribute_selection ==  4:
        print("'Kendini korumayi bilen, saldirmayi da bilendir.' dedigini duyar gibiyim. Sana katildigim noktalar oldugunu soylersem yalan olmaz sanirim.\n")
        Character.defence = Character.defence + 3
        update_character_json(character_name,Character.defence)
    elif attribute_selection ==  5:
        print("Insanlar sana surekli 'Niye bu kadar agresifsin {}?' diye sorsa da hala akillanmaya niyetin yok degil mi? Seni daha da sevdim!\n".format(character_name))
        Character.attack = Character.attack + 3
        update_character_json(character_name,Character.attack)
        print("+3 saldiri kazandin.")
    elif attribute_selection ==  6:
        print("Lutfen bana 'Hayat okulundan mezun oldum ben.' geyikleri yapma olur mu? Fakat hakkini vermem lazim, bazen bir darbe yuzlerce laftan daha fazla ders almani saglar.")
        Character.experience = Character.experience + 50
        update_character_json(character_name,Character.experience)
        print("+50 tecrube kazandin.")
    else:
        print("Isleri bu kadar zorlastirmak zorunda misin? Secenekler arasindan sec!")

#Func for item decision
def player_build_2(character_name):
    print("\n\nGuzel, seni simdiden tanimaya basladim {}. Bag kurmaya baslayip ilerisi icin guzel adimlar atiyoruz bile. Peki suan sahip olmak istedigin sey ne?".format(character_name))
    while True: 
        try: 
            selection_range = range(1,3)
            attribute_selection = int(input("1 - Cift Hancer\n2 - Cift El Kilic/Balta\n3 - Ok\n4 - Kalkan\n5 - Asa\n6 - Kalkan\n7 - Zirh\n8 - Para\n\n\n>>>"))
            if attribute_selection in selection_range:
                break
            else:
                print("Hadi ama! Sana basit 8 secenek sundum. Senin secimin olan {} ve bunlardan biri olmadigini sen de biliyor olmalisin, UMARIM!".format(attribute_selection))
        except ValueError:
            print("Bu kadar zor degil. Odaklanmaya calis!\nSana verdigim seceneklerden bir tanesini sec.")

# Main func
def new_game():
    character_name = player_name()
    player_build_1(character_name)
    player_build_2(character_name)