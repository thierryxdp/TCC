def uppCons(frase):
    """recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas e as vogais da mesma forma como estavam"""
    indice = 0
    frasetolist = [frase]
    while indice<len(frasetolist):
    	if str(frasetolist[indice]) in "aeiou" or str(frasetolist[indice]) in "AEIOU":
        	indice+=1
    	else:
            frasetolist[indice] = str.upper(frasetolist[indice])
            indice+=1
    return frasetolist