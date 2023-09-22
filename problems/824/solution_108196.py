def uppCons(frase):
    consoantes = "bcdfghjklmnpqrstvwxyz"
	return "".join([char if char in consoantes else char.upper() for char in frase])