# player classes
class defender: # add armor enchantments
    def __init__(self,helmet,chestplate,leggings,boots,entity_type):
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.entity_type = entity_type
        #health = entityHealthDict.get(entity_type)
        armor_points = 0 #entityArmorDict.get(entity_type)
        ## to find out: if a mob has armor naturally, does that ovveride the armor value that it may have without armor?
        ## of note: code is currently built so that if an entity has armor, it adds on to the natural armor value
        armor_points = armor_points + get_armor_points(helmet)
        armor_points = armor_points + get_armor_points(chestplate)
        armor_points = armor_points + get_armor_points(leggings)
        armor_points = armor_points + get_armor_points(boots)

# error classes
class invalidArmorType(Exception):
    pass

class invalidWeaponType(Exception):
    pass
