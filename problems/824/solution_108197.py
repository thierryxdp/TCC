def uppCons(frase):
    consoantes = "bcdfghjklmnpqrstvwxyz"
	return "".join([char.upper() if char in consoantes else char for char in frase])