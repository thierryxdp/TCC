def uppCons(frase):
    """recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas e as vogais da mesma forma como estavam"""
    indice = 0
    contador = 0
    frasetolist = [frase]
    listaindices =[]
    while indice<len(frasetolist):
    	if frasetolist[indice] in "aeiou" or frasetolist[indice] in "AEIOU":
        	indice+=1
    	else:
        	listaindices+= [indice]
        	indice+=1
    while contador <len(listaindices):
        frasetolist[contador] = str.upper(frasetolist[contador])
        contador+=1
    return frasetolist