

import random
import time

class game:
	class gensettings:
		height = 25
		width = 25
	##dungeon variables
	dungeon = []
	popdungeon = []
	posx = (gensettings.width - 1)
	posy = (gensettings.height)
	oldx = (gensettings.width - 2)
	oldy = (gensettings.height - 1)

	minenemies = 1
	maxenemies = 3
	#lower = harder
	diff = 10

	def nav(x, y):
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
		game.dungeon[game.oldy][game.oldx] = "b"
		game.oldx = curx
		game.oldy = cury

		##current location
		tmpdun[cury][curx] = "PL"

		if l == "c" or l == "b":
			opts = (opts + "Left (L) | ")
		if r == "c" or r == "b":
			opts = (opts + "Right (R) | ")
		if t == "c" or t == "b":
			opts = (opts + "Forward (F) | ")
		if b == "c" or b == "b":
			opts = (opts + "Backward (B) | ")

		printMaze(tmpdun)

		##get enemy count
		enimies = game.popdungeon[cury][curx]
		if enimies == "0" or str(enimies).__contains__(" "):
			enimies = "no"
		print("There are " + enimies + " enemies in this room")

		print("You may go: " + opts)
		choice = input()

		if str(choice.lower()).__contains__("l") and l != "w":
			game.posx = ((curx - 1) + 1)
			game.posy = ((cury) + 1)
		elif str(choice.lower()).__contains__("r") and r != "w":
			game.posx = ((curx + 1) + 1)
			game.posy = ((cury) + 1)
		elif str(choice.lower()).__contains__("f") and t != "w":
			game.posx = ((curx) + 1)
			game.posy = ((cury - 1) + 1)
		elif str(choice.lower()).__contains__("b") and b != "w":
			game.posx = ((curx) + 1)
			game.posy = ((cury + 1) + 1)




## Functions
def printMaze(maze):
	for i in range(0, game.gensettings.height):
		for j in range(0, game.gensettings.width):
			if (maze[i][j] == 'u'):
				print(str(maze[i][j]), end="")
			elif (maze[i][j] == 'c'):
				print(str(maze[i][j]).replace("c","  "), end="")
			elif (maze[i][j] == 'b'):
				print(str(maze[i][j]).replace("b","  "), end="")
			else:
				print(str(maze[i][j]).replace("w","██"), end="")
			
		print('')

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
			maze[0][i] = '░░'
			break

	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == 'c'):
			maze[height-1][i] = '░░'
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
					pop = (str(pop) + " ")
				else:
					pop = "  "
				line.append(pop)
			popmaze.append(line)
		game.popdungeon = popmaze
		printMaze(popmaze)
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
	

				


genmaze()
popmaze(0,3)

game.nav(game.posx, game.posy)
##loop = True
##while loop:
##	game.nav(game.posx, game.posy)

