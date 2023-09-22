def uppCons(frase):
    alfabeto = 1
    frase_final = frase[0].upper()
    while alfabeto < len(frase):
        if frase[alfabeto] in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
            frase_final += frase[alfabeto].upper()
        if frase[alfabeto] in ('C'):
            	frase_final += frase[alfabeto].lower()
        alfabeto += 1
	return frase_final

def uppCons(frase):
    alfabeto = 1
    frase_final = frase[0].upper()
    while alfabeto < len(frase):
        if frase[alfabeto] in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
            frase_final += frase[alfabeto].upper()
        else:
            frase_final += frase[alfabeto].lower()
        alfabeto += 1
	return frase_final