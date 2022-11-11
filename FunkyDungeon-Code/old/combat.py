import math
import random



defaulthealth = 100
playeritems = [
    ["healpot", 3, ["hp", "heals 25 hp instantly"]], 
    ["defencepot", 1, ["def", "decreases damage taken by 20 percent for 1 turn"]],
    ["cocaine", 1, ["atk", "increases damage dealt by 20 percent for 1 turn"]],
    ["shinyrock", 1, ["dis", "distracts the enemy and allows you to flee"]]
]

playerwep = [
    "Axe", 25, "Sword", 30
]
enemywep = [
    "Rock", 20, "Mace", 40
]


def bar(max, cur, title, disptype,):
    bartext = "["
    finalbar = ""


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

def weapons(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff):
    print("------------------------------------------------------")
    print("Weapons")
    print("------------------------------------------------------")
    weapondmgs = []
    weaponnames = []
    curwep = 0

    for x in playerwep:
        if isinstance(x ,int):
            weapondmgs.append(x)
        else:
            weaponnames.append(x)
    for x in weaponnames:
        print("Name: " + x + " | Damage: " + str(weapondmgs[curwep]))
        curwep = (curwep + 1)
    print("------------------------------------------------------")
    use = input("Weapon Name | Back (B) ")
    if use.lower() == "b":
        battle(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff, "player")
    curwep = 0
    for x in weaponnames:
        if str(x).lower() == use.lower():
            crit = random.randint(1, 10)
            if crit == 10:
                wep = x
                wepdmg = weapondmgs[curwep]
                wepdmg = (wepdmg + ((wepdmg / 100) * 15))
                print("------------------------------------------------------")
                print("Critical Hit! You Dealt 15 Percent Extra Damage To " + enemyname + " With Your " + wep + " Dealing " + str(wepdmg) + " Damage")
                print("------------------------------------------------------")

                battle(playerhp ,maxplayerhp ,(enemyhp - wepdmg), maxenemyhp, enemyname, run, item, False, defbuff, "enemy")
            elif atkbuff:
                wep = x
                wepdmg = weapondmgs[curwep]
                wepdmg = (wepdmg + ((wepdmg / 100) * 20))
                print("------------------------------------------------------")
                print("You Dealt 20 Percent Extra Damage To " + enemyname + " With Your " + wep + " Dealing " + str(wepdmg) + " Damage")
                print("------------------------------------------------------")

                battle(playerhp ,maxplayerhp ,(enemyhp - wepdmg) ,maxenemyhp ,enemyname ,run ,item ,False ,defbuff, "enemy" )
            else:
                wep = x
                wepdmg = weapondmgs[curwep]
                print("------------------------------------------------------")
                print("You Attacked " + enemyname + " With Your " + wep + " Dealing " + str(wepdmg) + " Damage")
                print("------------------------------------------------------")

                battle(playerhp ,maxplayerhp ,(enemyhp - wepdmg), maxenemyhp, enemyname, run, item, atkbuff, defbuff, "enemy")
        curwep = (curwep + 1)

def items(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff):
    print("------------------------------------------------------")
    print("Items")
    print("------------------------------------------------------")
    for x in playeritems:
        for y in x:
            if isinstance(y, str):
                itemname = y
            if isinstance(y, int):
                print("Name: " + itemname + " | Count: " + str(y) + " | Info: " + x[2][1])
    print("------------------------------------------------------")
    use = input("Item Name | Back (B) ")
    if use.lower() == "b":
        battle(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff, "player")
    type = ""
    for x in playeritems:    
        if isinstance(x[0], str):
                if str(x[0]).lower() == use.lower():
                    type = x[2][0]
                    useitem = x[0]
                    x[1] = (x[1] - 1)
    if type == "hp":
        if (playerhp + 25) >= maxplayerhp:
            playerhp = 100
        else:
            playerhp = (playerhp + 25)
        print("------------------------------------------------------")
        print("You Consumed 1 " + useitem + " And Gained 25 Health")
        print("------------------------------------------------------")
        battle(playerhp, maxplayerhp, enemyhp, maxenemyhp, enemyname, run, True, False, False, "player")
    if type == "def":
        print("------------------------------------------------------")
        print("You Consumed 1 " + useitem + " And Gained 20 Percent Extra Defence For 1 Turn")
        print("------------------------------------------------------")
        battle(playerhp, maxplayerhp, enemyhp, maxenemyhp, enemyname, run, True, False, True, "player")
    if type == "atk":
        print("------------------------------------------------------")
        print("You Consumed 1 " + useitem + " And Gained 20 Percent Extra Attack For 1 Turn")
        print("------------------------------------------------------")
        battle(playerhp, maxplayerhp, enemyhp, maxenemyhp, enemyname, run, True, True, False, "player")
    if type == "dis":
        print("------------------------------------------------------")
        print("You Threw 1 " + useitem + " And Gained The Oppurtunity To Sneak Away")
        print("------------------------------------------------------")
        battle(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, True, True, False, False, "player")

def endbattle(win, name):
    if win:
        print("------------------------------------------------------")
        print("You Won The Fight Against " + name)
        print("------------------------------------------------------")
    if win == False:
        print("------------------------------------------------------")
        print("You Lost The Fight Against " + name)
        print("------------------------------------------------------")
    if win == None:
        print("------------------------------------------------------")
        print("You Fled From The Fight Against " + name)
        print("------------------------------------------------------")
def battle(playerhp, maxplayerhp, enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff, turn):

    if enemyhp <= 0:
        enemyhp = 0
        endbattle(True, enemyname)
    elif playerhp <= 0:
        playerhp = 0
        endbattle(False, enemyname)
    
    def playerturn(playerhp, maxplayerhp, enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff):
        print("------------------------------------------------------")
        bar(maxenemyhp, enemyhp ,enemyname , 3)
        bar(maxplayerhp, playerhp, "You", 3)
        print("------------------------------------------------------")
        opts = "Weapon (W) | "
        if item == True:
            opts = (opts + "Item (I) | ")
        if run == True:
            opts = (opts + "Flee (F)")
    
        print(opts)
        print("------------------------------------------------------")
        opt = input("Pick One... ")
        if opt.lower() == "w":
            weapons(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff)
        elif opt.lower() == "i" and item == True:
            items(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff,)
        elif opt.lower() == "f" and run == True:
            endbattle(None, enemyname)
            

    def enemyturn(playerhp, maxplayerhp, enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff):
        print("------------------------------------------------------")
        bar(maxenemyhp, enemyhp ,enemyname , 3)
        bar(maxplayerhp, playerhp, "You", 3)
        print("------------------------------------------------------")
        opts = "You Cant Act Right Now."
        print(opts)
        print("------------------------------------------------------")
        weapondmgs = []
        weaponnames = []
        curwep = 0
        wepdmg = 0

        for x in enemywep:
            if isinstance(x ,int):
                weapondmgs.append(x)
            else:
                weaponnames.append(x)
        for x in weaponnames:
            print("Name: " + x + " | " + str(weapondmgs[curwep]))
            curwep = (curwep + 1)
        print("------------------------------------------------------")
        use = random.choice(weaponnames)
        curwep = 0
        for x in weaponnames:
            if str(x).lower() == str(use).lower():
                crit = random.randint(1, 10)
                if crit == 10:
                    wep = x
                    wepdmg = weapondmgs[curwep]
            crit = random.randint(1, 10)
            if crit == 10:
                wepdmg = weapondmgs[curwep]
                wep = x
                wepdmg = (wepdmg + ((wepdmg / 100) * 15))
                print("------------------------------------------------------")
                print("Critical Hit! " + enemyname + " Dealt 15 Percent Extra Damage To You With " + wep + " Dealing " + str(wepdmg) + " Damage")
                print("------------------------------------------------------")

                battle((playerhp - wepdmg) ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff, "player")
            elif defbuff:
                wepdmg = weapondmgs[curwep]
                wep = x
                wepdmg = (wepdmg - ((wepdmg / 100) * 20))
                print("------------------------------------------------------")
                print(enemyname + " Dealt 20 Percent Less Damage To You With " + wep + " Dealing " + str(wepdmg) + " Damage")
                print("------------------------------------------------------")

                battle((playerhp - wepdmg) ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, False, "player")
            else:
                wepdmg = weapondmgs[curwep]
                wep = x
                print("------------------------------------------------------")
                print(enemyname + " Attacked You With " + wep + " Dealing " + str(wepdmg) + " Damage")
                print("------------------------------------------------------")

                battle((playerhp - wepdmg) ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff, "player")
        

    if str(turn).lower() == "player":
        playerturn(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff)
    if str(turn).lower() == "enemy":
        enemyturn(playerhp ,maxplayerhp ,enemyhp, maxenemyhp, enemyname, run, item, atkbuff, defbuff)


def encounter(name, loc, startbattle, playerhealth ,enemyhealth, run, item):
    print("------------------------------------------------------")
    print("You encountered " + name + " in the " + loc)
    print("------------------------------------------------------")
    if startbattle:
        battle(playerhealth ,playerhealth ,enemyhealth, enemyhealth, name, run, item, False, False, "player")
    


encounter("ExampleName", "The   Oven", True, defaulthealth, 100, True, True)