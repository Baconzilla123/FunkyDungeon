###TO DO#######
#MAKE CODE NOT SPAGHET
#FIX ITEM SELECTION

import random
import time

class titlescreen:
    titleart = [
        "░▒█▀▀▀░█░▒█░█▀▀▄░█░▄░█░░█░░░▒█▀▀▄░█░▒█░█▀▀▄░█▀▀▀░█▀▀░▄▀▀▄░█▀▀▄",
        "░▒█▀▀░░█░▒█░█░▒█░█▀▄░█▄▄█░░░▒█░▒█░█░▒█░█░▒█░█░▀▄░█▀▀░█░░█░█░▒█",
        "░▒█░░░░░▀▀▀░▀░░▀░▀░▀░▄▄▄▀░░░▒█▄▄█░░▀▀▀░▀░░▀░▀▀▀▀░▀▀▀░░▀▀░░▀░░▀",
        " ",
        "                     [Press Enter To Play]"
    ]
    def selectdiff():
        print("---------------------------------------------------------------")
        game.diff = int(input("Difficulty (lower = harder): "))
        if int(game.diff) < 1 or int(game.diff) > 10:
            print("The Difficulty May Not Be Set Below 1 Or Above 10, Please Try Again.")
            titlescreen.selectdiff()
        
        print("---------------------------------------------------------------")
        lobby.enterlobby()

    def screen():
        for line in titlescreen.titleart:
            print(line)
            time.sleep(0.1)
        pressplay = input()
        time.sleep(1)
        titlescreen.selectdiff()
        
        
class game:
    class gensettings:
        height = 25
        width = 25
    ##dungeon variables
    dungeon = []
    popdungeon = []

    minenemies = 1
    maxenemies = 3
    #lower = harder
    diff = 5

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

    def room(size, extop, exleft, exright):
        topbot = ""
        room = []
        loop = size
        while loop > 0:
            if loop == 1 or size:
                loop = size
                while loop > 0:
                    topbot = (topbot + "#")

                room.append(topbot)
            

            loop = (loop - 1)
        for draw in room:
            print(draw)
    
    def maze(maze):
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

class player:
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
                item = ([itemname, iteminfo, itemtype, count])
                hasitem = True
                break
            else:
                hasitem = False
        if hasitem == False:
            item = ([itemname, iteminfo, itemtype, 1])
        player.invitems.append(item)

    def addweapon(weaponname, weaponinfo, weapontype):
        weapon = ([weaponname, weaponinfo,weapontype])
        player.invweapons.append(weapon)

class combat:
    ename = ""
    ehp = 0
    mehp = 0
    ws = []

    def enter(enemyname, maxenemyhp, curenemyhp, weaponset):
        combat.ename = enemyname
        combat.ehp = curenemyhp
        combat.mehp = maxenemyhp
        combat.ws = weaponset

        combat.player()

    def attack(weapon):
        crit = random.randint(1, 10)
        if crit == 10:
            wepdmg = weapon[2]
            wepdmg = (wepdmg + ((wepdmg / 100) * 15))
            print("------------------------------------------")
            print("Critical Hit! You Dealt 15 Percent Extra Damage To " + combat.ename + " With Your " + weapon[0] + " Dealing " + str(wepdmg) + " Damage")
            print("------------------------------------------")
        elif player.atkbuff:
            wepdmg = weapon[2]
            wepdmg = (wepdmg + ((wepdmg / 100) * 20))
            print("------------------------------------------")
            print("You Dealt 20 Percent Extra Damage To " + combat.ename + " With Your " + weapon[0] + " Dealing " + str(wepdmg) + " Damage")
            print("------------------------------------------")
            player.atkbuff = False
        else:
            wepdmg = weapon[2]
            print("------------------------------------------")
            print("You Attacked " + combat.ename + " With Your " + weapon[0] + " Dealing " + str(wepdmg) + " Damage")
            print("------------------------------------------")
        combat.ehp = combat.ehp - wepdmg
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
                    print("------------------------------------------------------")
                    print("You Consumed 1 " + useitem + " And Gained 25 Health")
                    print("------------------------------------------------------")

                if type == "def":
                    print("------------------------------------------------------")
                    print("You Consumed 1 " + useitem + " And Gained 20 Percent Extra Defence For 1 Turn")
                    print("------------------------------------------------------")
                    player.defbuff = True
                if type == "atk":
                    print("------------------------------------------------------")
                    print("You Consumed 1 " + useitem + " And Gained 20 Percent Extra Attack For 1 Turn")
                    print("------------------------------------------------------")
                    player.atkbuff = True
                if type == "dis":
                    print("------------------------------------------------------")
                    print("You Threw 1 " + useitem + " And Gained The Oppurtunity To Sneak Away")
                    print("------------------------------------------------------")
                    player.canrun = True
        combat.player()


    def player():
        if player.hp <= 0:
            print("------------------------------------------")
            print("You Were Killed By", combat.ename + ",", "Game Over!")
            print("------------------------------------------")
            time.sleep(3)
            exit()
        print("------------------------------------------")
        render.bar(combat.mehp, combat.ehp, combat.ename, 3)
        render.bar(player.hpcap, player.hp, "You", 3)
        print("------------------------------------------")
        choice = input("Weapon (W) | Item (I) | Run (R) ")
        if str(choice).lower().__contains__("r"):
            if player.canrun == True:
                print("------------------------------------------")
                print("You Fled From The Fight Against", combat.ename + ".")
                print("------------------------------------------")
            else:
                print("------------------------------------------")
                print("You Can't Run Right Now... Maybe You Need A Distraction?")
                print("------------------------------------------")
                combat.player()


        #weapon selection
        if str(choice).lower().__contains__("w"):
        
            print("------------------------------------------")
            print("Weapons")
            print("------------------------------------------")
            for weapon in player.invweapons:
                print("Name:", weapon[0], "| Damage:", weapon[2])
            print("------------------------------------------")
            weaponchoice = input("Weapon (Name) | Back (B)")
            if str(weaponchoice).lower() == "b":
                combat.player()
            for getchoice in player.invweapons:
                if str(getchoice[0]).lower() == str(weaponchoice).lower():
                    combat.attack(getchoice)
                if str(getchoice[0]).lower().__contains__(weaponchoice.lower()):
                    combat.attack(getchoice)
                
            print("Please Enter The Name Of A Weapon You Actually Have :]")
            combat.player()

        #item selection
        elif str(choice).lower().__contains__("i"):
            print("------------------------------------------")
            print("Items")
            print("------------------------------------------")
            for item in player.invitems:
                print("Name:", item[0], "| Info:", item[1], "| Count:", item[3])
            print("------------------------------------------")
            itemchoice = input("Item (Name) | Back (B)")
            if str(itemchoice).lower() == "b":
                combat.player()
            for getchoice in player.invitems:
                if str(getchoice[0]).lower().__contains__(itemchoice.lower()):
                    combat.item(getchoice)
                
            print("Please Enter The Name Of An Item You Actually Have :]")
            combat.player()

    def enemy():
        if combat.ehp <= 0:
            print("------------------------------------------")
            print("You Won The Fight Against " + str(combat.ename) + " And Were Rewarded with 25G!")
            print("------------------------------------------")
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
            print("------------------------------------------")
            print("Critical Hit! " + combat.ename + " Dealt 15 Percent Extra Damage To You With Its " + atk[0] + " Dealing " + str(wepdmg) + " Damage")
            print("------------------------------------------")
        elif player.defbuff:
            wepdmg = atk[2]
            wep = atk[0]
            wepdmg = (wepdmg - ((wepdmg / 100) * 20))
            print("------------------------------------------")
            print(combat.ename + " Dealt 20 Percent Less Damage To You With " + wep + " Dealing " + str(wepdmg) + " Damage")
            print("------------------------------------------")
            player.defbuff = False
        else:
            wepdmg = atk[2]
            print("------------------------------------------")
            print(combat.ename + " Attacked You With Its " + atk[0] + " Dealing " + str(wepdmg) + " Damage")
            print("------------------------------------------")
        player.hp = player.hp - wepdmg
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

        # Initialize colorama


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
                        popch = random.randint(0,game.diff)
                        if popch == 1:
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
        if game.dungeon[player.posy - 1][player.posx - 1] == "w":
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
            combat.enter("Enemy", 100, 100, game.weapons)

    def gameloop():
        while player.indungeon:
            dungeon.nav(player.posx,player.posy)
            if player.posy == 1 and player.posx == 2:
                print("you completed a dungeon and were rewarded with 25 Gold!")
                player.bal = (player.bal + 25)
                choice = input("Continue (C) | Lobby (L)")
                if str(choice.lower()).__contains__("c"):
                    player.posx = (game.gensettings.width - 2)
                    player.posy = (game.gensettings.height - 1)
                    player.oldx = (game.gensettings.width - 2)
                    player.oldy = (game.gensettings.height - 1)
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

        print("----------------------------------")
        print("Item Shop                      " + str(player.bal) + "G")
        print("----------------------------------")
        for item in game.items:
            itemnames.append(item[0])
            itemprices.append(item[1])
            iteminfos.append(item[2])
            itemtypes.append(item[3])
        for itemname in itemnames:

            print("Name: " + itemname + " | Price: " + str(itemprices[current]) + "G | Info: " + iteminfos[current])
            current = (current + 1)
        print("----------------------------------")
        choice = str(input("Buy (Name) | Back (B)"))
        current = 0
        
        if choice.lower() == "b":
            lobby.enterlobby()

        for findbuy in itemnames:
            if str(findbuy).lower().__contains__(choice.lower()):
                if (player.bal - itemprices[current]) < (-1):
                    print("----------------------------------")
                    print(player.talkingto + ": You dont have enough money for that!")
                    print("----------------------------------")
                else:
                    player.additem(itemnames[current], iteminfos[current], itemtypes[current])
                    player.bal = (player.bal - itemprices[current])
                    print("----------------------------------")
                    print(player.talkingto + ": You Have Bought a " + itemnames[current] + " For " + str(itemprices[current]) + "G!")
                    print("----------------------------------")
                print(str(player.invitems))
                shop.returntoshop("items")
                break
            current = (current + 1)

        print("----------------------------------")
        print(player.talkingto + ": Please Enter The Name Of An Item.")
        print("----------------------------------")
        shop.returntoshop("items")
                
            

    def weaponshop():

        weaponnames = []
        weaponprices = []
        weaponinfos = []
        weapontypes = []
        current = 0

        print("----------------------------------")
        print("Weapon Shop                      " + str(player.bal) + "G")
        print("----------------------------------")
        for weapon in game.weapons:
            weaponnames.append(weapon[0])
            weaponprices.append(weapon[1])
            weaponinfos.append(weapon[2])
            
        for weaponname in weaponnames:

            print("Name: " + weaponname + " | Price: " + str(weaponprices[current]) + "G | Dmg: " + str(weaponinfos[current]))
            current = (current + 1)
        print("----------------------------------")
        choice = str(input("Buy (Name) | Back (B)"))
        current = 0
        
        if choice.lower() == "b":
            lobby.enterlobby()
        elif choice:
            for findbuy in weaponnames:
                if str(findbuy).lower().__contains__(choice.lower()):
                    if (player.bal - weaponprices[current]) < (-1):
                        print("----------------------------------")
                        print(player.talkingto + ": You dont have enough money for that!")
                        print("----------------------------------")
                    else:
                        player.addweapon(weaponnames[current], weaponprices[current], weaponinfos[current])
                        player.bal = (player.bal - weaponprices[current])
                        print("----------------------------------")
                        print(player.talkingto + ": You Have Bought a " + weaponnames[current] + " For " + str(weaponprices[current]) + "G!")
                        print("----------------------------------")
                    shop.returntoshop("weapons")
                    break
                current = (current + 1)

            print("----------------------------------")
            print(player.talkingto + ": Please Enter The Name Of An Item.")
            print("----------------------------------")
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
        '██                                                                ██',
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
        '██│    N    │                   PL                     │         │██',
        '██│    S    │                                          │         │██',
        '██│         │                                          │         │██',
        '██│         │                                          │         │██',
        '██│         │                                          │         │██',
        '██│         │                                          │         │██',
        '██└─────────┘                                          └─────────┘██',
        '████████████████████████████████████████████████████████████████████',


    ]
    inlobby = True
    def enterlobby():
        lobby.inlobby = True
        lobby.lobby()
    def lobby():
        for line in lobby.lobbyart:
            print(line)
        print("Welcome To The Lobby")
        print("Enjoy Your Stay :]")
        print("---------------------------")
        action = input("Enter The Dungeon (E) | Visit Weapons Shop (W) | Visit Items Shop (I)")
        if action.lower().__contains__("e"):
            dungeon.enter()
        if action.lower().__contains__("w"):
            shop.weaponshop()
        if action.lower().__contains__("i"):
            shop.itemshop()
        

##Testing Area##
#combat.enter("Joe Biden", 100, 50, game.weapons)

##Game Start##
titlescreen.screen()

