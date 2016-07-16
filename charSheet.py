class Sheet:

    def __init__(self,**kwargs):

        if kwargs:
            self.g_info = kwargs["g_info"]
            self.ab_scores = kwargs["ab_scores"]

        else:
            self.ab_scores = {
            "str":0,
            "dex":0,
            "con":0,
            "int":0,
            "wis":0,
            "cha":0
            }

            self.g_info = {
                "name":"no name",
                "race":"no race",
                "char_class":"no class",
                "alignment":"no alignment",
                "background":"no background",
                "lvl":1,
                "exp":0,

                "p_bonus":0,
                "s_throws":"none",
                "skills":"none",

                "ac":0,
                "initiative":0,
                "speed":0,
                "hp":0,
                "tmp_hp":0,
                "hit_die":"1d6"
            }
