class Sheet:

    def __init__(self,**kwargs):
        if kwargs:
            self.name = kwargs["name"]
            self.race = kwargs["race"]
            self.char_class = kwargs["char_class"]
            self.alignment = kwargs["alignment"]
            self.background = kwargs["background"]
            self.lvl = kwargs["lvl"]
            self.exp = kwargs["exp"]

            self.base_stats = kwargs["base_stats"]
            self.bonus_stats = kwargs["bonus_stats"]
            self.total_stats = kwargs["total_stats"]

            self.p_bonus = kwargs["p_bonus"]
            self.s_throws = kwargs["s_throws"]
            self.skills = kwargs["skills"]


            self.ac = kwargs["ac"]
            self.initiative = kwargs["initiative"]
            self.speed = kwargs["speed"]
            self.hp = kwargs["hp"]
            self.tmp_hp = kwargs["tmp_hp"]
            self.hit_die = kwargs["hit_die"]
        else:
            self.base_stats = {
            "str":0,
            "dex":0,
            "con":0,
            "int":0,
            "wis":0,
            "cha":0
            }
            self.bonus_stats = {
            "str":0,
            "dex":0,
            "con":0,
            "int":0,
            "wis":0,
            "cha":0
            }
            self.total_stats = {
            "str":0,
            "dex":0,
            "con":0,
            "int":0,
            "wis":0,
            "cha":0
            }
            self.name = "no name"
            self.race = "no race"
            self.char_class = "no class"
            self.alignment = "no alignment"
            self.background = "no background"
            self.lvl = 1
            self.exp = 0

            self.p_bonus = 0
            self.s_throws = "none"
            self.skills = "none"

            self.ac = 0
            self.initiative = 0
            self.speed = 0
            self.hp = 0
            self.tmp_hp = 0
            self.hit_die = "1d6"

    def updateBonusStat(self,stat,val):
        self.bonus_stats[stat] = val
        print self.bonus_stats[stat]
