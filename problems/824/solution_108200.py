def uppCons(frase):
    consoantes = "bcççdfghjklmnpqrstvwxyz"
	return "".join([char.upper() if char in consoantes else char for char in frase])