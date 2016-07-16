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
        print "Type in your character's information. "
        for line in self.sheet.g_info.keys():
            myinput = raw_input(line+": ")
            self.sheet.g_info[line] = myinput

        print "Type in your character's ability scores without bonuses. "
        for stat in self.sheet.ab_scores.keys():
            myinput = raw_input(stat+":")
            self.sheet.ab_scores[stat] = myinput


    def retrieveSheet(self,filename):
        if not os.path.isfile(filename):
            print "Character sheet does not exist."
            create = raw_input("Create new?[Y/n]")
            if create == 'Y':
                self.updateSheet(self,filename,self.initCharacter)
            elif create == 'n':
                print "No new file created."
            else:
                print "Not a valid option. Aborting."
        else:
            fid = open(filename,'r')
            self.sheet = json.load(fid,object_hook=dict2obj)
            fid.close()


    def updateSheet(self,filename,func):
        loop_cond = True
        while(loop_cond):
            if os.path.isfile(filename):
                o_write = raw_input("Character sheet already exists. Overwrite?[Y/n]")
                if o_write == 'Y':
                    func()
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


    def updateInfo(self):
        stat = raw_input("What do you want to update? ")
        if stat in self.sheet.g_info.keys():
            self.sheet.g_info[stat] = raw_input(stat +": ")
        else:
            self.sheet.ab_scores[stat] = raw_input(stat +": ")


myInterface = Interface()
#retrive before update to prevent wiping previous save
myInterface.retrieveSheet("test2.json")
myInterface.updateSheet("test2.json",myInterface.updateInfo)

pp = pprint.PrettyPrinter(indent=1,width=1)
pp.pprint(myInterface.sheet.ab_scores)
