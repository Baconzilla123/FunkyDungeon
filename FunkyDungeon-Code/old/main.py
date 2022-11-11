
import random

class game:

    items = [
        ["Health Potion", 10, "Heals 15 hp Instantly", "hel"],
        ["Defence Potion", 15, "Gives 20 Percent Less Damage Taken For 1 Turn", "def"],
        ["Damage Potion", 15, "Gives 20 Percent More Damage Dealt For 1 Turn", "atk"],
        ["Shiny Rock", 20, "Distracts The Enemy, Allowing You To Flee", "dis"],
        ["Arrow (16)", 5, "Ammo For Bows Or Crossbows", 16],
        ]
    weapons = [
            ["Axe", 15, "Chop", 20],
            ["Mace", 20, "Bonk", 25],
            ["Sword", 30, "Stab", 30],
            ["Brick", 100, "Crack", 2],
            ["Bow", 25, "Pew", 10],
            ["Crossbow", 35, "Better Bow", 15]
        ]

class render:
    def bar(max, cur, title, disptype,):
        bartext = "["
        finalbar = ""
        prefixbar = False

        if title:
            prefixbar = True
        
        percent = ((cur / max) * 100)
        
        barloop = (percent / 5)
        loop = barloop
        while loop > 0:
            loop = (loop - 1)
            bartext = (bartext + "#")

        loop = ((100 / 5) - barloop)

        while loop > 0:
            loop = (loop - 1)
            bartext = (bartext + "=")

        bartext = (bartext + "]")

        if prefixbar == True:
            finalbar = (title + ": " + bartext)
        else:
            finalbar = (bartext)

        if disptype == 1:
            finalbar = (finalbar + " " + str(percent) + "%")
        elif disptype == 2:
            finalbar = (finalbar + " " + str(cur))
        elif disptype == 3:
            finalbar = (finalbar + " " + str(cur) + "/" + str(max))

        print(finalbar)
    def inv():
        for item in player.invitems:
            print(item)
            
class player:
    atkbuff = False
    defbuff = False
    canrun = False
    canskip = True

    bal = 100
    hp = 50
    hpcap = 100

    talkingto = ""

    invitems = [["Lesser Health Potion", 10, "Heals 10 hp Instantly", "hel"]]
    invweapons = []
    invammo = []

    def addammo(ammoname, ammocount):
        ammoadd = ([ammoname, ammocount])
        for ammo in player.invammo:
            if str(ammo).__contains__(ammoname):
                ammocount = (ammocount + ammo[1])
                player.invammo.remove(ammo)
                
        player.invammo.append(ammoadd)

    def additem(itemname, iteminfo, itemtype):
        item = ([itemname, iteminfo,itemtype])
        player.invitems.append(item)
                

    def addweapon(weaponname, weaponinfo, weapontype):
        weapon = ([weaponname, weaponinfo,weapontype])
        player.invweapons.append(weapon)
        
class combat:
    class actions:
        pass

class shop:

    buycap = 10
    lastsell = []

    def returntoshop(shopname):
        if shopname == "weapons":
            choice = input("Return To Weapons Shop? (Y/N)")
            if choice.lower() == "y": shop.weaponshop()
            if choice.lower() == "n": pass
        if shopname == "items":
            choice = input("Return To Items Shop? (Y/N)")
            if choice.lower() == "y": shop.itemshop()
            if choice.lower() == "n": pass

    def itemshop():

        itemnames = []
        itemprices = []
        iteminfos = []
        itemtypes = []
        current = 0

        print("------------------------------------------------------")
        print("Item Shop                      " + str(player.bal) + "G")
        print("------------------------------------------------------")
        for item in game.items:
            itemnames.append(item[0])
            itemprices.append(item[1])
            iteminfos.append(item[2])
            itemtypes.append(item[3])
        for itemname in itemnames:

            print("Name: " + itemname + " | Price: " + str(itemprices[current]) + "G | Info: " + iteminfos[current])
            current = (current + 1)
        print("------------------------------------------------------")
        choice = str(input("Buy (Name) | Back (B)"))
        current = 0
        
        if choice.lower() == "b":
            pass

        for findbuy in itemnames:
            if str(findbuy).lower().__contains__(choice.lower()):
                if (player.bal - itemprices[current]) < (-1):
                    print("------------------------------------------------------")
                    print(player.talkingto + ": You dont have enough money for that!")
                    print("------------------------------------------------------")
                else:
                    if itemtypes[current] == int:
                        player.addammo(itemnames[current], iteminfos[current])
                    player.additem(itemnames[current], iteminfos[current], itemtypes[current])
                    player.bal = (player.bal - itemprices[current])
                    print("------------------------------------------------------")
                    print(player.talkingto + ": You Have Bought a " + itemnames[current] + " For " + str(itemprices[current]) + "G!")
                    print("------------------------------------------------------")
                shop.returntoshop("items")
                
            current = (current + 1)

    def weaponshop():

        weaponnames = []
        weaponprices = []
        weaponinfos = []
        weapontypes = []
        current = 0

        print("------------------------------------------------------")
        print("Weapon Shop                      " + str(player.bal) + "G")
        print("------------------------------------------------------")
        for weapon in game.weapons:
            weaponnames.append(weapon[0])
            weaponprices.append(weapon[1])
            weaponinfos.append(weapon[2])
            weapontypes.append(weapon[3])
        for weaponname in weaponnames:

            print("Name: " + weaponname + " | Price: " + str(weaponprices[current]) + "G | Info: " + weaponinfos[current])
            current = (current + 1)
        print("------------------------------------------------------")
        choice = str(input("Buy (Name) | Back (B)"))
        current = 0
        
        if choice.lower() == "b":
            pass
        elif choice:
            for findbuy in weaponnames:
                if str(findbuy).lower().__contains__(choice.lower()):
                    if (player.bal - weaponprices[current]) < (-1):
                        print("------------------------------------------------------")
                        print(player.talkingto + ": You dont have enough money for that!")
                        print("------------------------------------------------------")
                    else:
                        player.addweapon(weaponnames[current], weaponinfos[current], weapontypes[current])
                        player.bal = (player.bal - weaponprices[current])
                        print("------------------------------------------------------")
                        print(player.talkingto + ": You Have Bought a " + weaponnames[current] + " For " + str(weaponprices[current]) + "G!")
                        print("------------------------------------------------------")
                    shop.returntoshop("weapons")
                    
                current = (current + 1)
                
class dialogue:
    current = 0
    def msg(speak, message):
        print(speak + ": " + message)
    def opt(speak, message ,type):
        if type == "weaponshop":
            player.talkingto = speak
            shop.weaponshop()
        if type == "itemshop":
            player.talkingto = speak
            shop.itemshop()
        print(speak + ": " + message)
        choice = input("Visit (V) | Dont Visit (D)")
        if choice.lower == "v":
            if type == "weaponshop":
                shop.weaponshop()
            if type == "itemshop":
                shop.itemshop()
    
class nav:
    def travel(type, dirs):
        if type == 0:
            if str(dirs).__contains__("n"):
                opts = (opts + "N | ")
            if str(dirs).__contains__("e"):
                opts = (opts + "E | ")
            if str(dirs).__contains__("s"):
                opts = (opts + "S | ")
            if str(dirs).__contains__("w"):
                opts = (opts + "W | ")
            choice = input(opts)


