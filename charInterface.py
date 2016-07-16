from charSheet import Sheet
from json_obj_conv import convert_to_builtin_type as obj2dict
from json_obj_conv import dict_to_object as dict2obj
import json
import os.path
import pprint
class Interface:
    def __init__(self,**kwargs):
        self.sheet = Sheet()
    def initCharacter(self):
        self.sheet.name = raw_input("What is your character's name? ")
        self.sheet.race = raw_input("What is your character's race? ")
        self.sheet.char_class = raw_input("What class are you? ")
        self.sheet.alignment = raw_input("What is your alignment? ")
        self.sheet.background = raw_input("What is your character's background? ")
        self.sheet.lvl = raw_input("What is your level? ")
        self.sheet.exp = raw_input("How much experience do you have? ")

        stat_list = self.sheet.total_stats.keys()
        print "Type in the stat followed by any bonuses for the listed ability. Ex: 14 2"
        for stat in stat_list:
            input = raw_input(stat+":")
            input = input.split()
            base,bonus = int(input[0]),int(input[1])
            self.sheet.base_stats[stat],self.sheet.bonus_stats[stat]=\
            base,bonus
            self.sheet.total_stats[stat] = base+bonus

        self.sheet.p_bonus = 0
        self.sheet.s_throws = 0
        self.sheet.skills = 0

        self.sheet.ac = raw_input("What is your AC? ")
        self.sheet.initiative = raw_input("What is your initiative? ")
        self.sheet.speed = raw_input("What is your speed? ")
        self.sheet.maxhp = raw_input("What is your max health? ")
        self.sheet.hp = 0
        self.sheet.tmp_hp = 0
        self.sheet.hit_die = raw_input("What is your hit die? ")

    def retrieveSheet(self,filename):
        if not os.path.isfile(filename):
            print "Character sheet does not exist."
        else:
            fid = open(filename,'r')
            self.sheet = json.load(fid,object_hook=dict2obj)
            fid.close()
            #return mysheet
    def createSheet(self,filename):
        loop_cond = True
        while(loop_cond):
            if os.path.isfile(filename):
                o_write = raw_input("Character sheet already exists. Overwrite?[Y/n]")
                print o_write
                if o_write == 'Y':
                    self.initCharacter()
                    fid = open(filename,"wb")
                    json.dump(obj2dict(self.sheet),fid)
                    fid.close()
                    loop_cond = False
                elif o_write == 'n':
                    print "Overwrite aborted."
                    loop_cond = False
                else:
                    print "Not a valid option."
            else:
                fid = open(filename,"wb")
                json.dump(obj2dict(self.sheet),fid)
                fid.close()
                loop_cond = False
'''    def updateSheet(self,filename,param_list):
        loop_cond = True
        while(loop_cond):
            if os.path.isfile(filename):
                o_write = raw_input("Character sheet already exists. Overwrite?[Y/n]")
                print o_write
                if o_write == 'Y':

                    fid = open(filename,"wb")
                    json.dump(obj2dict(self.sheet),fid)
                    fid.close()
                    loop_cond = False
                elif o_write == 'n':
                    print "Overwrite aborted."
                    loop_cond = False
                else:
                    print "Not a valid option."
            else:
                fid = open(filename,"wb")
                json.dump(obj2dict(self.sheet),fid)
                fid.close()
                loop_cond = False
'''
myInterface = Interface()
myInterface.createSheet("test1.json")
myInterface.retrieveSheet("test1.json")
pp = pprint.PrettyPrinter(indent=1,width=1)
pp.pprint(myInterface.sheet.total_stats)
