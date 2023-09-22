def uppCons(frase):
    i = 0
    cons = ''
    while i < len(frase):
        if not (frase[i] in "AEIOUaeiouáíóúãé"):
            cons += frase[i].upper()
        else:
        	cons += frase[i]
        i += 1
	return cons