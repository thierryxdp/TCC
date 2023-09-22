listaConsoantes = [1,2,3]

def uppCons(frase):
    for i in range(len(frase)):
        frase = [i]
        if frase in listaConsoantes:
            frase = frase.uppercase
	return frase