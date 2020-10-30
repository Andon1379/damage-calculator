armorEnchDict = {
    "protection" : 4, # caps at 80%, max effective level is 20, stacks with other proc enchants, applied after normal armor protection
    "fire protection" : 8, # caps at 80%, stacks with other procs
    "projectile protection": 8, # caps at 80% 
    "blast protection": 8, # caps at 80%
    "feather falling": 12, # fall damage reduction is 12% per level, caps at 80%, stacks w/ proc, includes ender perals
    "fire proc time reduction java": 15 # only matters for highenst level of fire proc
    }
# percentile damage nullification per level (EPF) 
# proj. proc reduces damage from: arrows, thrown tridents, shulker bullets, llama spit, blaze fireballs
# proj. proc reduces direct damage from: ghast fireballs, wither skulls
# damage from splash pots of harming, dragon fireballs, or fireworks are not reduced by proj proc (the first of which is reduced by proc, however)
# in java, proc doesnt help with void or hunger damage. in bedrock, it also does not help with status effects like poison or wither. otherwise, damage is reduced by proc  
