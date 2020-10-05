import random

def rolld(faces):
	"Rolls a d-faces die"
	if faces not in [4, 6, 8, 10, 12, 20]:
		raise Exception("Must be a regular sided die.")
	return random.randint(1, faces)

def rollnd(n, faces):
	"Rolls n faces dice"
	if not isinstance(n, int) or n < 1:
		raise Exception("Must roll at least one die.")
	rolls = []
	for i in range(n):
		rolls.append(rolld(faces))	
	return rolls
