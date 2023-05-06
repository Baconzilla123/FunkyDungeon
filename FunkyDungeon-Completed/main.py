
import random
import time
import os
import json

class titlescreen:
    titleart = [
        "░▒█▀▀▀░█░▒█░█▀▀▄░█░▄░█░░█░░░▒█▀▀▄░█░▒█░█▀▀▄░█▀▀▀░█▀▀░▄▀▀▄░█▀▀▄",
        "░▒█▀▀░░█░▒█░█░▒█░█▀▄░█▄▄█░░░▒█░▒█░█░▒█░█░▒█░█░▀▄░█▀▀░█░░█░█░▒█",
        "░▒█░░░░░▀▀▀░▀░░▀░▀░▀░▄▄▄▀░░░▒█▄▄█░░▀▀▀░▀░░▀░▀▀▀▀░▀▀▀░░▀▀░░▀░░▀",
        " ",
        "                     [Press Enter To Play]"
    ]
    def selectsave():
        print("---------------------------------------------------------------")
        save.load()
        print("---------------------------------------------------------------")
        if player.modded == True:
            mods.load()
        else:
            print("Mods Are Disabled For This Player, Loading Normally...")
        time.sleep(0.5)
        lobby.enterlobby()

    def screen():
        for line in titlescreen.titleart:
            print(line)
            time.sleep(0.1)
        pressplay = input()
        time.sleep(1)
        titlescreen.selectsave()
        

class mods:
    dir = "./Mods"
    files = []

    def load():
        

        f = []
        for (dirpath, dirnames, filenames) in os.walk(mods.dir):
            f.extend(filenames)
            for filename in filenames:
                if filename.endswith(".fdmod"):
                    mods.files.append(filename)
            break
        if len(mods.files)  > 0:
            print("Loading Mods...")
        else:
            print("No Mods Found, Loading Normally...")
    
        for mod in mods.files:
            with open(mods.dir + "/" + mod, "r") as modfile:
                moddata = json.load(modfile)

                print("Loading Mod: " + moddata["modname"])
                for item in moddata["moditems"]:
                    game.items.append(item)
                    print("["+ moddata["modname"] + "] loaded item: " + item[0])
                for weapon in moddata["modweapons"]:
                    game.weapons.append(weapon)
                    print("["+ moddata["modname"] + "] loaded weapon: " + weapon[0])
                for enemy in moddata["modenemies"]:
                    game.enemies.append(enemy)
                    print("["+ moddata["modname"] + "] loaded enemy: " + enemy["name"])
   
class save:
    savedir = "./Saves"
    files = []
    saves = []
    diff = 0
    modded = False
    def load():
        save.saves = []
        save.files = []
        f = []
        for (dirpath, dirnames, filenames) in os.walk(save.savedir):
            f.extend(filenames)
            for filename in filenames:
                if filename.endswith(".fdsave"):
                    save.files.append(filename)
            break
        for savefile in save.files:
            
            with open(save.savedir + "/" + savefile, "r") as file:
                savedata = json.load(file)
                savebox = [
                    "╔═══════════════════════════════╦═══════╗",
                    f'║ {savedata["name"]: <30}║ {str(savedata["bal"]) + "G": <6}║',
                    "╚═══════════════════════════════╩═══════╝ ",
                ]
                for line in savebox:
                    print(line)
                    
                save.saves.append(savedata)
        print("")
        selsave = input("Create Save (C) | Load Save (Name) : ")
        if selsave.lower() == "c":
            save.create()
        else:
            found = False
            for savefile in save.saves:
                if str(savefile["name"]).rstrip(".fdsave").lower().__contains__(str(selsave).lower()):
                    found = True
                    player.modded = savefile["modded"]
                    
                    player.name = savefile["name"]
                    player.cursave = savefile["name"] + ".fdsave"
                    print("Loaded save: " + str(player.cursave))
                    player.atkbuff = savefile["atkbuff"]
                    player.defbuff = savefile["defbuff"]
                    player.canrun = savefile["canrun"]
                    player.canskip = savefile["canskip"]

                    game.diff = savefile["diff"]

                    player.bal = savefile["bal"]
                    player.hp = savefile["hp"]
                    player.hpcap = savefile["hpcap"]

                    player.talkingto = savefile["talkingto"]

                    player.invitems = savefile["invitems"]
                    player.invweapons = savefile["invweapons"]
                    time.sleep(0.3)
                else:
                    if found == False:
                        found = False
            if found != True:
                print("Save not found, Please try again.")
                save.load()

    def save():
        savedata = {
            "modded":player.modded,

            "name":player.name,
            "cursave":player.cursave,
            "atkbuff":player.atkbuff,
            "defbuff":player.defbuff,
            "canrun":player.canrun,
            "canskip":player.canskip,

            "diff":game.diff,

            "bal":player.bal,
            "hp":player.hp,
            "hpcap":player.hpcap,

            "talkingto":player.talkingto,

            "invitems":player.invitems,
            "invweapons":player.invweapons
        }
        savejson = json.dumps(savedata)
        with open(save.savedir + "/" + player.cursave, "w") as file:
            file.truncate(0)
            file.write(savejson)
                
    def create():
        name = input("Enter the name of this save: ")
        def seldiff():
            save.diff = int(input("Enter the difficulty of this save (1-10): "))
            if int(save.diff) < 1 or int(save.diff) > 10:
                print("The Difficulty May Not Be Set Below 1 Or Above 10, Please Try Again.")
                seldiff()
        def modded():
            save.modded = input("Enable mods (Y/N): ")
            if str(save.modded).lower() == "y":
                save.modded = True
            elif str(save.modded).lower() == "n":
                save.modded = False
            else:
                print("You must answer y or n, Please try again")
                modded()

        seldiff()
        modded()

        savedata = {
            "modded":save.modded,

            "name":name,
            "cursave":name + ".fdsave",
            "atkbuff":False,
            "defbuff":False,
            "canrun":False,
            "canskip":True,

            "diff":save.diff,

            "bal":100,
            "hp":100,
            "hpcap":100,

            "talkingto":"",

            "invitems":[
                ["Health Potion", "Heals 15 hp Instantly", "hel", 5]
            ],
            "invweapons":[
                    ["Shank", 1, 15]
            ]
        }
        savejson = json.dumps(savedata)
        with open(save.savedir + "/" + savedata["cursave"], "x") as file:
            file.truncate(0)
            file.write(savejson)
        save.load()

class game:
    class gensettings:
        height = 25
        width = 25
    

    ##dungeon variables
    dungeon = []
    popdungeon = []

    minenemies = 1
    maxenemies = 3
    #1-10
    diff = 5

    enemies = [
        {
            "name":"Archer",
            "health":75,
            "weapons":[
                ["Bow", 25, 10],
                ["Crossbow", 35, 15]
            ],
        },
        {
            "name":"Possesed Skeleton",
            "health":50,
            "weapons":[
                ["Axe", 25, 20],
                ["Rock", 35, 10],
                ["Sharpened Bone", 1, 15]
            ],
        },
        {
            "name":"Explorer",
            "health":100,
            "weapons":[
                ["Pickaxe", 25, 10],
                ["Sword", 35, 30]
            ],
        },
        {
            "name":"Buff Rat",
            "health":30,
            "weapons":[
                ["Brick", 100, 2],
                ["Brick", 100, 2],
                ["Brick", 100, 2],
                ["Brick", 100, 2],
                ["Brick", 100, 2],
                ["Boulder", 35, 30]
            ],
        },
    ]

    items = [
        ["Health Potion", 10, "Heals 15 hp Instantly", "hel"],
        ["Defence Potion", 15, "Gives 20 Percent Less Damage Taken For 1 Turn", "def"],
        ["Damage Potion", 15, "Gives 20 Percent More Damage Dealt For 1 Turn", "atk"],
        ["Shiny Rock", 20, "Distracts The Enemy, Allowing You To Flee", "dis"],
        ]
    weapons = [
            ["Axe", 15, 20],
            ["Mace", 20, 25],
            ["Sword", 30, 30],
            ["Brick", 100, 2],
            ["Bow", 25, 10],
            ["Crossbow", 35, 15]
        ]

class render:
    def clear():
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
    
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

        return finalbar
    
    def maze(maze):
        os.system("cls")
        for i in range(0, game.gensettings.height):
            for j in range(0, game.gensettings.width):
                if (maze[i][j] == 'u'):
                    print(str(maze[i][j]), end="")
                elif (maze[i][j] == 'c'):
                    print(str(maze[i][j]).replace("c","  "), end="")
                elif (maze[i][j] == 'b'):
                    print(str(maze[i][j]).replace("b","  "), end="")
                elif (maze[i][j] == 'e'):
                    print(str(maze[i][j]).replace("e","░░"), end="")
                else:
                    print(str(maze[i][j]).replace("w","██"), end="")
                
            print('')

    def box(txt):
        txtw = len(txt)
        boxline = ""
        for char in range(txtw + 3):
            boxline = boxline + "═"
        box = [
            f"╔{boxline}╗",
            f'║ {txt}  ║',
            f"╚{boxline}╝ ",
        ]
        for line in box:
            print(line)

class player:
    modded = False

    name = "Player"
    cursave = "SaveFile"

    atkbuff = False
    defbuff = False
    canrun = False
    canskip = True

    bal = 100
    hp = 100
    hpcap = 100

    talkingto = ""

    invitems = [
        ["Health Potion", "Heals 15 hp Instantly", "hel", 5],
    ]
    invweapons = [
        ["Shank", 1, 15]
    ]

    ##dungeon pos variables
    posx = (game.gensettings.width - 1)
    posy = (game.gensettings.height)
    oldx = (game.gensettings.width - 2)
    oldy = (game.gensettings.height - 1)
    indungeon = False

    def additem(itemname, iteminfo, itemtype):
        hasitem = False
        ##check if add to stack of item
        for item in player.invitems:
            if itemname == item[0]:
                count = (item[3] + 1)
                newitem = ([itemname, iteminfo, itemtype, count])
                hasitem = True
                item[3] = count
                break
            else:
                hasitem = False
        if hasitem == False:
            newitem = ([itemname, iteminfo, itemtype, 1])
            player.invitems.append(newitem)

    def addweapon(weaponname, weaponinfo, weapontype):
        weapon = ([weaponname, weaponinfo,weapontype])
        player.invweapons.append(weapon)

class combat:
    comdel = 0.3
    ename = ""
    ehp = 0
    mehp = 0
    ws = []

    def enter():


        enemy = random.choice(game.enemies)
        combat.ename = enemy["name"]
        combat.ehp = int(enemy["health"])
        combat.mehp = int(enemy["health"])
        combat.ws = enemy["weapons"]

        combat.player()

    def attack(weapon):
        crit = random.randint(1, 10)
        if crit == 10:
            wepdmg = weapon[2]
            wepdmg = (wepdmg + ((wepdmg / 100) * 15))
            
            render.box("Critical Hit! You Dealt 15 Percent Extra Damage To " + combat.ename + " With Your " + weapon[0] + " Dealing " + str(wepdmg) + " Damage")
            
        elif player.atkbuff:
            wepdmg = weapon[2]
            wepdmg = (wepdmg + ((wepdmg / 100) * 20))
            
            render.box("You Dealt 20 Percent Extra Damage To " + combat.ename + " With Your " + weapon[0] + " Dealing " + str(wepdmg) + " Damage")
            
            player.atkbuff = False
        else:
            wepdmg = weapon[2]
            
            render.box("You Attacked " + combat.ename + " With Your " + weapon[0] + " Dealing " + str(wepdmg) + " Damage")
            
        combat.ehp = combat.ehp - wepdmg
        time.sleep(combat.comdel)
        combat.enemy()

    def item(item):
        for finditem in player.invitems:
            if str(item[0]) == str(finditem[0]):
                type = item[2]
                useitem = item[0]
                finditem[3] = (finditem[3] - 1)
                if finditem[3] == 0:
                    player.invitems.remove(item)
                if type == "hel":
                    if (player.hp + 25) >= player.hpcap:
                        player.hp = 100
                    else:
                        player.hp = (player.hp + 25)

                    render.box("You Consumed 1 " + useitem + " And Gained 25 Health")
                    

                if type == "def":
                    
                    render.box("You Consumed 1 " + useitem + " And Gained 20 Percent Extra Defence For 1 Turn")
                    
                    player.defbuff = True
                if type == "atk":
                    
                    render.box("You Consumed 1 " + useitem + " And Gained 20 Percent Extra Attack For 1 Turn")
                    
                    player.atkbuff = True
                if type == "dis":
                    
                    render.box("You Threw 1 " + useitem + " And Gained The Oppurtunity To Sneak Away")
                    
                    player.canrun = True
        time.sleep(combat.comdel)
        combat.player()


    def player():
        if player.hp <= 0:
            
            render.box("You Were Killed By " + combat.ename + ", " + "Game Over!")
            
            time.sleep(3)
            exit()
        
        
        playerbar = render.bar(player.hpcap, player.hp, player.name, 3)
        enemybar = render.bar(combat.mehp, combat.ehp, combat.ename, 3)

        maxlen = 0
        if len(playerbar) > maxlen:
            maxlen = len(playerbar) + 1
        if len(enemybar) > maxlen:
            maxlen = len(enemybar) + 1
        descline = "═"
        space = " "
        for char in range(maxlen):
            descline = descline + "═"
        uigrid = [
            "╔═" + descline + "═╗",
            f"║ Combat {str(space): <{maxlen - 6}} ║",
            "╠═" + descline + "═╣",
        ]
        
        for line in uigrid:
            print(line)
        
        print(f'║ {playerbar: <{maxlen}}  ║')
        print(f'║ {enemybar: <{maxlen}}  ║')
        
        
        print("╚═" + descline + "═╝")
        
        
        choice = input("Weapon (W) | Item (I) | Run (R) ")
        if str(choice).lower().__contains__("r"):
            if player.canrun == True:
                
                render.box("You Fled From The Fight Against" + str(combat.ename) + ".")
                time.sleep(1.5)
                player.indungeon = True
                game.popdungeon[(player.posy - 1)][(player.posx - 1)] = (int(game.popdungeon[(player.posy - 1)][(player.posx - 1)]) - 1)
                dungeon.gameloop()
            else:
                
                render.box("You Can't Run Right Now... Maybe You Need A Distraction?")
                
                time.sleep(combat.comdel)
                combat.player()


        #weapon selection
        if str(choice).lower().__contains__("w"):
        
            uigrid = [
                "╔═════════════════════════════════════════════╗",
                "║ Weapons                                     ║",
                "╠═════════════════════╦═══════════╦═══════════╣",
            ]
            for line in uigrid:
                print(line)
            for weapon in player.invweapons:
                NAME = weapon[0]
                COST = weapon[1]
                DMG = weapon[2]
                section = f'║ {NAME: <20}║ {str(COST) + "G": <10}║ {str(DMG) + "DMG": <10}║'
                print(section)
            
            
            print("╚═════════════════════╩═══════════╩═══════════╝")
            
            weaponchoice = input("Weapon (Name) | Back (B)")
            if str(weaponchoice).lower() == "b":
                combat.player()
            for getchoice in player.invweapons:
                if str(getchoice[0]).lower() == str(weaponchoice).lower():
                    combat.attack(getchoice)
                if str(getchoice[0]).lower().__contains__(weaponchoice.lower()):
                    combat.attack(getchoice)
                
            render.box("Please Enter The Name Of A Weapon You Actually Have :]")
            time.sleep(combat.comdel)
            combat.player()

        #item selection
        if str(choice).lower().__contains__("i"):
            maxlen = 0
            for item in player.invitems:
                
                if len(item[1]) > maxlen:
                    maxlen = len(item[1]) + 1
            descline = "═"
            space = " "
            for char in range(maxlen):
                descline = descline + "═"
            uigrid = [
                "╔═════════════════════" + descline + "══════╗",
                f"║ Items               {str(space): <{maxlen}}       ║",
                "╠════════════════════╦" + descline + "╦═════╣",
            ]
            
            for line in uigrid:
                print(line)
            for item in player.invitems:
                NAME = item[0]
                DESC = item[1]
                AMNT = item[3]
                section = f'║ {NAME: <19}║ {str(DESC): <{maxlen}}║ {"x" + str(AMNT): <4}║'
                print(section)
            
            
            print("╚════════════════════╩" + descline + "╩═════╝")
            
            #for item in player.invitems:
            #    print("Name:", item[0], "| Info:", item[1], "| Count:", item[3])
            
            itemchoice = input("Item (Name) | Back (B)")
            if str(itemchoice).lower() == "b":
                combat.player()
            for getchoice in player.invitems:
                if str(getchoice[0]).lower().__contains__(itemchoice.lower()):
                    combat.item(getchoice)
                
            render.box("Please Enter The Name Of An Item You Actually Have :]")
            time.sleep(combat.comdel)
            combat.player()

    def enemy():
        
        if combat.ehp <= 0:
            
            render.box("You Won The Fight Against " + str(combat.ename) + " And Were Rewarded with 25G!")
            
            time.sleep(1.5)
            player.indungeon = True
            game.popdungeon[(player.posy - 1)][(player.posx - 1)] = (int(game.popdungeon[(player.posy - 1)][(player.posx - 1)]) - 1)
            dungeon.gameloop()
        time.sleep(1.5)
        atk = random.choice(combat.ws)
        crit = random.randint(1, 10)
        if crit == 10:
            wepdmg = atk[2]
            wepdmg = (wepdmg + ((wepdmg / 100) * 15))
            
            render.box("Critical Hit! " + combat.ename + " Dealt 15 Percent Extra Damage To You With Its " + atk[0] + " Dealing " + str(wepdmg) + " Damage")
            
        elif player.defbuff:
            wepdmg = atk[2]
            wep = atk[0]
            wepdmg = (wepdmg - ((wepdmg / 100) * 20))
            
            render.box(combat.ename + " Dealt 20 Percent Less Damage To You With " + wep + " Dealing " + str(wepdmg) + " Damage")
            
            player.defbuff = False
        else:
            wepdmg = atk[2]
            
            render.box(combat.ename + " Attacked You With Its " + atk[0] + " Dealing " + str(wepdmg) + " Damage")
            
        player.hp = player.hp - wepdmg
        time.sleep(combat.comdel)
        combat.player()

class dungeon:
    def genmaze():

        # Find number of surrounding cells
        def surroundingCells(rand_wall):
            s_cells = 0
            if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
                s_cells += 1
            if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
                s_cells += 1
            if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
                s_cells +=1
            if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                s_cells += 1

            return s_cells


        ## Main code
        # Init variables
        wall = 'w'
        cell = 'c'
        unvisited = 'u'
        height = game.gensettings.height
        width = game.gensettings.width
        maze = []


        # Denote all cells as unvisited
        for i in range(0, height):
            line = []
            for j in range(0, width):
                line.append(unvisited)
            maze.append(line)

        # Randomize starting point and set it a cell
        starting_height = int(random.random()*height)
        starting_width = int(random.random()*width)
        if (starting_height == 0):
            starting_height += 1
        if (starting_height == height-1):
            starting_height -= 1
        if (starting_width == 0):
            starting_width += 1
        if (starting_width == width-1):
            starting_width -= 1

        # Mark it as cell and add surrounding walls to the list
        maze[starting_height][starting_width] = cell
        walls = []
        walls.append([starting_height - 1, starting_width])
        walls.append([starting_height, starting_width - 1])
        walls.append([starting_height, starting_width + 1])
        walls.append([starting_height + 1, starting_width])

        # Denote walls in maze
        maze[starting_height-1][starting_width] = 'w'
        maze[starting_height][starting_width - 1] = 'w'
        maze[starting_height][starting_width + 1] = 'w'
        maze[starting_height + 1][starting_width] = 'w'

        while (walls):
            # Pick a random wall
            rand_wall = walls[int(random.random()*len(walls))-1]

            # Check if it is a left wall
            if (rand_wall[1] != 0):
                if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                    # Find the number of surrounding cells
                    s_cells = surroundingCells(rand_wall)

                    if (s_cells < 2):
                        # Denote the new path
                        maze[rand_wall[0]][rand_wall[1]] = 'c'

                        # Mark the new walls
                        # Upper cell
                        if (rand_wall[0] != 0):
                            if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])


                        # Bottom cell
                        if (rand_wall[0] != height-1):
                            if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])

                        # Leftmost cell
                        if (rand_wall[1] != 0):	
                            if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])
                    

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Check if it is an upper wall
            if (rand_wall[0] != 0):
                if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

                    s_cells = surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        maze[rand_wall[0]][rand_wall[1]] = 'c'

                        # Mark the new walls
                        # Upper cell
                        if (rand_wall[0] != 0):
                            if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])

                        # Leftmost cell
                        if (rand_wall[1] != 0):
                            if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])

                        # Rightmost cell
                        if (rand_wall[1] != width-1):
                            if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Check the bottom wall
            if (rand_wall[0] != height-1):
                if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

                    s_cells = surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        maze[rand_wall[0]][rand_wall[1]] = 'c'

                        # Mark the new walls
                        if (rand_wall[0] != height-1):
                            if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[1] != 0):
                            if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])
                        if (rand_wall[1] != width-1):
                            if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)


                    continue

            # Check the right wall
            if (rand_wall[1] != width-1):
                if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

                    s_cells = surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        maze[rand_wall[0]][rand_wall[1]] = 'c'

                        # Mark the new walls
                        if (rand_wall[1] != width-1):
                            if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])
                        if (rand_wall[0] != height-1):
                            if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[0] != 0):	
                            if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Delete the wall from the list anyway
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)
            


        # Mark the remaining unvisited cells as walls
        for i in range(0, height):
            for j in range(0, width):
                if (maze[i][j] == 'u'):
                    maze[i][j] = 'w'

        # Set entrance and exit
        for i in range(0, width):
            if (maze[1][i] == 'c'):
                maze[0][i] = 'e'
                break

        for i in range(width-1, 0, -1):
            if (maze[height-2][i] == 'c'):
                maze[height-1][i] = 's'
                break
        game.dungeon = maze

    def popmaze():
        def enemies(min,max):
            line = []
            prntline = ""
            popmaze = []
            for row in game.dungeon:
                line = []
                for cell in row:
                    if cell == "c":
                        
                        popch = random.randint(game.diff,10)
                        if popch == 10:
                            pop = random.randint(min, max)
                        else:
                            pop = 0
                        pop = (str(pop))
                    else:
                        pop = " "
                    line.append(pop)
                popmaze.append(line)
            game.popdungeon = popmaze
        def loot():
            def lootroom():
                try: 
                    game.dungeon[ypos - 1][xpos - 1] = lootchar
                    game.dungeon[ypos - 1][xpos] = lootchar
                    game.dungeon[ypos][xpos - 1] = lootchar
                    game.dungeon[ypos + 1][xpos + 1] = lootchar
                    game.dungeon[ypos + 1][xpos] = lootchar
                    game.dungeon[ypos][xpos + 1] = lootchar
                    game.dungeon[ypos][xpos] = lootchar
                    game.dungeon[ypos][xpos] = lootchar
                    game.dungeon[ypos][xpos] = lootchar
                    game.dungeon[ypos - 1][xpos + 1] = lootchar
                    game.dungeon[ypos + 1][xpos - 1] = lootchar
                except IndexError:
                    loot()
            hxpos = 0
            lxpos = 0
            hypos = 0
            lypos = 0
            lootchar = "▒▒"
            areas = ["t"]
            area = random.choice(areas)
            if area == "t":
                lypos = 3
                hypos = (game.gensettings.height)
                lxpos = 3
                hxpos = (game.gensettings.width)
            print(area)
            ypos = random.randint(lypos,hypos)
            xpos = random.randint(lxpos,hxpos)
            if xpos > game.gensettings.width / 2 and ypos > game.gensettings.height / 2:
                loot()
            else:
                lootroom()
            

            print(ypos, xpos)

        enemies(game.minenemies,game.maxenemies)

    def nav(x, y):
        if game.dungeon[player.posy - 1][player.posx - 1] == "w" or game.dungeon[0][1] == "w":
            print("Generation Error, Retrying...")
            dungeon.enter()
        canfight = False
        
        tmpdun = game.dungeon

        l = ""
        r = ""
        t = ""
        b = ""

        cury = (y - 1)
        curx = (x - 1)
        opts = ""

        try:
            l = game.dungeon[cury][(curx - 1)]
        except IndexError:
            pass
        try:
            r = game.dungeon[cury][(curx + 1)]
        except IndexError:
            pass
        try:
            t = game.dungeon[(cury - 1)][curx]
        except IndexError:
            pass
        try:
            b = game.dungeon[(cury + 1)][curx]
        except IndexError:
            pass

        ##set already discovered path
        game.dungeon[player.oldy][player.oldx] = "b"
        player.oldx = curx
        player.oldy = cury

        ##current location
        tmpdun[cury][curx] = "PL"
        print("coordinates: ", curx, " ", cury)

        if l == "c" or l == "b":
            opts = (opts + "Left (L) | ")
        if r == "c" or r == "b":
            opts = (opts + "Right (R) | ")
        if t == "c" or t == "b":
            opts = (opts + "Forward (F) | ")
        if b == "c" or b == "b":
            opts = (opts + "Backward (B) | ")

        render.maze(tmpdun)

        ##get enemy count
        enemies = game.popdungeon[cury][curx]
        if enemies == "0" or str(enemies).__contains__(" "):
            enemies = "no"
        print("There are " + str(enemies) + " enemies in this room")
        if enemies != "no":
            if int(enemies) > 0:
                canfight = True
            else:
                canfight = False
        else:
            canfight = False
        if canfight == True:
            opts = (opts + "Fight An Enemy In This Room (E) | ")

        print("You may go: " + opts)
        choice = input()

        #multimove
        moves = choice.split(",")
        if len(moves) > 1:
            for move in moves:
                if str(move.lower()).__contains__("l") and l != "w":
                    player.posx = ((curx - 1) + 1)
                    player.posy = ((cury) + 1)
                elif str(move.lower()).__contains__("r") and r != "w":
                    player.posx = ((curx + 1) + 1)
                    player.posy = ((cury) + 1)
                elif str(move.lower()).__contains__("f") and t != "w":
                    player.posx = ((curx) + 1)
                    player.posy = ((cury - 1) + 1)
                elif str(move.lower()).__contains__("b") and b != "w":
                    player.posx = ((curx) + 1)
                    player.posy = ((cury + 1) + 1)
                else:
                    print("You ran into a wall :[")
                    break
        #move
        if str(choice.lower()).__contains__("l") and l != "w":
            player.posx = ((curx - 1) + 1)
            player.posy = ((cury) + 1)
        elif str(choice.lower()).__contains__("r") and r != "w":
            player.posx = ((curx + 1) + 1)
            player.posy = ((cury) + 1)
        elif str(choice.lower()).__contains__("f") and t != "w":
            player.posx = ((curx) + 1)
            player.posy = ((cury - 1) + 1)
        elif str(choice.lower()).__contains__("b") and b != "w":
            player.posx = ((curx) + 1)
            player.posy = ((cury + 1) + 1)
        elif str(choice.lower()).__contains__("e") and canfight == True:
            combat.enter()
        #wasd movement
        elif str(choice.lower()).__contains__("a") and l != "w":
            player.posx = ((curx - 1) + 1)
            player.posy = ((cury) + 1)
        elif str(choice.lower()).__contains__("d") and r != "w":
            player.posx = ((curx + 1) + 1)
            player.posy = ((cury) + 1)
        elif str(choice.lower()).__contains__("w") and t != "w":
            player.posx = ((curx) + 1)
            player.posy = ((cury - 1) + 1)
        elif str(choice.lower()).__contains__("s") and b != "w":
            player.posx = ((curx) + 1)
            player.posy = ((cury + 1) + 1)

    def gameloop():
        while player.indungeon:
            dungeon.nav(player.posx,player.posy)
            if player.posy == 1 and player.posx == 2:
                print("you completed a dungeon and were rewarded with 25 Gold!")
                player.bal = (player.bal + 25)
                choice = input("Continue (C) | Lobby (L)")
                player.posx = (game.gensettings.width - 2)
                player.posy = (game.gensettings.height - 1)
                player.oldx = (game.gensettings.width - 2)
                player.oldy = (game.gensettings.height - 1)
                if str(choice.lower()).__contains__("c"):
                    dungeon.enter()
                if str(choice.lower()).__contains__("l"):
                    lobby.enterlobby()
                else:
                    print("An Option Was Not Selected, Returning To Lobby...")
                    lobby.enterlobby()
    
    def enter():
        dungeon.genmaze()
        dungeon.popmaze()
        player.indungeon = True
        dungeon.gameloop()
        
class shop:

    buycap = 10
    lastsell = []

    def returntoshop(shopname):
        if shopname == "weapons":
            choice = input("Return To Weapons Shop? (Y/N)")
            if choice.lower() == "y": shop.weaponshop()
            if choice.lower() == "n": lobby.enterlobby()
        if shopname == "items":
            choice = input("Return To Items Shop? (Y/N)")
            if choice.lower() == "y": shop.itemshop()
            if choice.lower() == "n": lobby.enterlobby()

    def itemshop():

        itemnames = []
        itemprices = []
        iteminfos = []
        itemtypes = []
        current = 0
        baltext = (str(player.bal) + "G")
        playerbal = f"{str(baltext): <5}"
        namelen = 0
        desclen = 0
        for item in game.items:
            if len(item[2]) > desclen:
                desclen = len(item[2]) + 1
            if len(item[0]) > namelen:
                namelen = len(item[0]) + 1
        
        nameline = "═"
        descline = "═"
        space = " "

        for char in range(desclen):
            descline = descline + "═"
        for char in range(namelen):
            nameline = nameline + "═"
        
        uigrid = [
            "╔" + nameline + "═" + descline + "╦═══════╗",
            f"║ Item Shop {' ': <{(desclen + namelen) - 8}}║ {playerbal} ║",
            "╠" + nameline + "╦" + descline + "╬═══════╣",
        ]
        
        for line in uigrid:
            print(line)
        for item in game.items:
            NAME = item[0]
            DESC = item[2]
            COST = item[1]
            section = f'║ {NAME: <{namelen}}║ {str(DESC): <{desclen}}║ {str(COST) + "G": <5} ║'
            print(section)
        
        
        print("╚" + nameline + "╩" + descline + "╩═══════╝")

        #print("----------------------------------")
        #print("Item Shop                      " + str(player.bal) + "G")
        #print("----------------------------------")
        for item in game.items:
            itemnames.append(item[0])
            itemprices.append(item[1])
            iteminfos.append(item[2])
            itemtypes.append(item[3])
        for itemname in itemnames:

            #print("Name: " + itemname + " | Price: " + str(itemprices[current]) + "G | Info: " + iteminfos[current])
            current = (current + 1)
        #print("----------------------------------")
        choice = str(input("Buy (Name) | Back (B)"))
        current = 0
        
        if choice.lower() == "b":
            lobby.enterlobby()

        for findbuy in itemnames:
            if str(findbuy).lower().__contains__(choice.lower()):
                if (player.bal - itemprices[current]) < (-1):
                    
                    render.box(player.talkingto + ": You dont have enough money for that!")
                    
                else:
                    player.additem(itemnames[current], iteminfos[current], itemtypes[current])
                    player.bal = (player.bal - itemprices[current])
                    
                    render.box(player.talkingto + ": You Have Bought a " + itemnames[current] + " For " + str(itemprices[current]) + "G!")
                    
                shop.returntoshop("items")
                break
            current = (current + 1)

        
        render.box(player.talkingto + ": Please Enter The Name Of An Item.")
        
        shop.returntoshop("items")        

    def weaponshop():

        weaponnames = []
        weaponprices = []
        weaponinfos = []
        weapontypes = []
        current = 0
        baltext = (str(player.bal) + "G")
        playerbal = f"{str(baltext): <5}"
        uigrid = [
                "╔══════════════════════════════════════╦═══════╗",
                f"║ Weapon Shop                          ║ {playerbal} ║",
                "╠═════════════════════╦═══════════╦════╩═══════╣",
            ]
        for line in uigrid:
            print(line)
        for weapon in game.weapons:
            NAME = weapon[0]
            COST = weapon[1]
            DMG = weapon[2]
            section = f'║ {NAME: <20}║ {str(COST) + "G": <10}║ {str(DMG) + "DMG": <11}║'
            print(section)
            
            
        print("╚═════════════════════╩═══════════╩════════════╝")

        #print("----------------------------------")
        #print("Weapon Shop                      " + str(player.bal) + "G")
        #print("----------------------------------")
        for weapon in game.weapons:
            weaponnames.append(weapon[0])
            weaponprices.append(weapon[1])
            weaponinfos.append(weapon[2])
            
        for weaponname in weaponnames:

            #print("Name: " + weaponname + " | Price: " + str(weaponprices[current]) + "G | Dmg: " + str(weaponinfos[current]))
            current = (current + 1)
        #print("----------------------------------")
        choice = str(input("Buy (Name) | Back (B)"))
        current = 0
        
        if choice.lower() == "b":
            lobby.enterlobby()
        elif choice:
            for findbuy in weaponnames:
                if str(findbuy).lower().__contains__(choice.lower()):
                    if (player.bal - weaponprices[current]) < (-1):
                        
                        render.box(player.talkingto + ": You dont have enough money for that!")
                        
                    else:
                        player.addweapon(weaponnames[current], weaponprices[current], weaponinfos[current])
                        player.bal = (player.bal - weaponprices[current])
                        
                        render.box(player.talkingto + ": You Have Bought a " + weaponnames[current] + " For " + str(weaponprices[current]) + "G!")
                        
                    shop.returntoshop("weapons")
                    break
                current = (current + 1)

            
            render.box(player.talkingto + ": Please Enter The Name Of An Item.")
            
            shop.returntoshop("weapons")

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

class lobby:
    lobbyart = [
        '██████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████████',
        '██                                                                ██',
        '██                     [Enter The Dungeon (E)]                    ██',
        '██                                                                ██',
        '██                                                                ██',
        '██                                                                ██',
        '██                                                                ██',
        '██┌─────────┐                                          ┌─────────┐██',
        '██│    W    │                                          │    I    │██',
        '██│    E    │                                          │    T    │██',
        '██│    A    │                                          │    E    │██',
        '██│    P    │                                          │    M    │██',
        '██│    O    │                                          │    S    │██',
        '██│    N    │                    PL                    │         │██',
        '██│    S    │                                          │         │██',
        '██│         │                                          │         │██',
        '██│         │                                          │         │██',
        '██│   (W)   │                                          │   (I)   │██',
        '██│         │              [Exit Game (G)]             │         │██',
        '██└─────────┘                                          └─────────┘██',
        '██████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████████',


    ]
    inlobby = True
    def enterlobby():
        render.clear()
        lobby.inlobby = True
        lobby.lobby()
    def lobby():
        for line in lobby.lobbyart:
            print(line)
        print("╔══════════════════════╗")
        print("║ Welcome To The Lobby ║")
        print("║ Enjoy Your Stay :]   ║")
        print("╚══════════════════════╝")
        action = input("")
        if action.lower().__contains__("e"):
            dungeon.enter()
        if action.lower().__contains__("w"):
            shop.weaponshop()
        if action.lower().__contains__("i"):
            shop.itemshop()
        if action.lower().__contains__("g"):
            saveinp = input("Save Progress (Y/N): ")
            if saveinp.lower() == "y":
                save.save()
                print("Saved to: " + str(player.cursave))
            exit("GoodBye! :D")


##Testing Area##
#combat.enter("Joe Biden", 100, 50, game.weapons)
##Game Start##

render.clear()

titlescreen.screen()

