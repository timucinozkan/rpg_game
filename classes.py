class Character(): 
    #Starting Stats
    current_health = 100
    health = 1
    agility = 1
    intelligent = 1
    strength = 1
    luck = 1
    defence = 1 
    attack = 1
    experience = 0

    # Characters progressed stats
    def __init__(self,character_name,character_current_health,character_health,character_agility,character_intelligent,character_strength,character_luck,character_defence,character_attack,character_experience):
        self.name = character_name
        self.current_health = character_current_health
        self.health = character_health
        self.agility = character_agility
        self.intelligent = character_intelligent
        self.strength = character_strength
        self.luck = character_luck
        self.defence = character_defence
        self.attack = character_attack
        self.experience = character_experience
