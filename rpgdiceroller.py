import random

def rolld(faces):
	"Rolls a d-sided die"
	if faces not in [4, 6, 8, 10, 12, 20, 100]:
		raise Exception("Must be a regular sided die, up to a d20.")
	return random.randint(1, faces)

def rollmod(faces, mod):
	"Rolls a faces-sided die with a modifier."
	if not isinstance(mod, int) or mod >= 10 or mod <= -5:
		raise Exception("Modifier must be between -5 and 10.")
	roll = rolld(faces)
	return roll+mod, roll

def rollnd(n, faces):
	"Rolls n faces-sided dice"
	if not isinstance(n, int) or n < 1:
		raise Exception("Must roll at least one die.")
	rolls = []
	for i in range(n):
		rolls.append(rolld(faces))
	return rolls

def rollad(faces):
	"Rolls a faces-sided die with advantage."
	rolls = rollnd(2, faces)
	return max(rolls), rolls

def rolldis(faces):
	"Rolls a faces-sided die with disadvantage."
	rolls = rollnd(2, faces)
	return min(rolls), rolls

def rolladmod(faces, mod):
	"Rolls a faces-sided die with advantage and mod modifier."
	rolls = rollmod(faces, mod), rollmod(faces, mod)
	return max(rolls), rolls

def rolldismod(faces, mod):
	"Rolls a faces-sided die with disadvantage and mod modifier."
	rolls = rollmod(faces, mod), rollmod(faces, mod)
	return min(rolls), rolls

def success(roll):
	if roll == 6: #Explode 6
		return 1 + success(rolld(6))
	elif roll in [4, 5]:
		  return 1
	elif roll in [2, 3]:
		return 0
	elif roll == 1:
		return -2
	else:
		raise Exception("Must roll a d6.")

def rollsuccesses(n):
	return sum(map(success, rollnd(n, 6)))
