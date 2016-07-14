class Sheet:

    def __init__(self,**kwargs):
        if kwargs:
            self.base_stats = kwargs["base_stats"]
            self.bonus_stats = kwargs["bonus_stats"]
            self.total_stats = kwargs["total_stats"]
        else:
            self.name = "No Name"
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
    def updateBonusStat(self,stat,val):
        self.bonus_stats[stat] = val
        print self.bonus_stats[stat]
