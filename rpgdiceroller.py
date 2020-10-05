import random

def rolld(faces):
	"Rolls a d-faces"
	if faces < 4:
		raise Exception("Die must have at least 4 faces.")
	return random.randint(1, faces)

def rollnd(n, faces):
	"Rolls n face dice"
	if n < 1:
		raise Exception("Must roll at least one die")
	rolls = []
	for i in range(n):
		rolls.append(rolld(faces))	
	return rolls
