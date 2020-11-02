# import armor dictionaries
from dicts.armor_dict import armorPtsDict as amPtsDic
from dicts.armor_dict import armorToughDict as amToughDic
# import weapon dictionaries
from dicts.melee_weapon_dict import javaMeleeWeaponDamageDict as jMDD
from dicts.melee_weapon_dict import bedrockMeleeWeaponDamageDict as bMDD
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

def get_weapon_damage(weapon_type = "none", game_ver = "java"):
    if type(weapon_type) == str:
        if game_ver == "java"
             return jMDD.get(weapon_type)
        if game_ver == "bedrock"
             return bMDD.get(weapon_type)  
    else:
        raise classes.invalidWeaponType

# assume full attack strength, add support for enchantments 
def calculate_damage(natural_points=0,helmet="none",chestplate="none",leggings="none",boots="none", weapon_type = "none", game_ver = "java 1.9+", is_crit=False, damage_type="melee"):
    ppv = total_armor(natural_points,helmet,chestplate,leggings,boots) * 0.8 # percentile protection value
    # java 1.9 math, in 1.8 each proc point adds 4% 
    if "java" in game_ver:
        damage = get_weapon_damage(weapon_type = "none", game_ver = "java")
    # damage = damage - ppv # NO-- there is an algorithim on armor wiki
    # return damage
    
