# import armor dictionaries
from dicts.armor_dict import armorPtsDict as amPtsDic
from dicts.armor_dict import armorToughDict as amToughDic
# import weapon dictionaries
# import enchantment dictionaries
from dicts.armor_enchants_dict import armorEnchDict as amEnDict
# import msc stuff
import classes

def get_armor_points(armor_type = "none"):
    if type(armor_type) == str:
        if armor_type == "none":
            return 0
        return amPtsDic.get(armor_type)   
    else:
        raise classes.invalidArmorType

def total_armor(natural_points=0,helmet="none",chestplate="none",leggings="none",boots="none"):
    total_points = natural_points
    total_points = total_points + get_armor_points(helmet)
    total_points = total_points + get_armor_points(chestplate)
    total_points = total_points + get_armor_points(leggings)
    total_points = total_points + get_armor_points(boots)
    return total_points

"""
def calculate_damage():
    pass
"""
