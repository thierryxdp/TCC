def uppCons(frase):
    """funcao que recebe uma frase como entrada e retorna a mesma frase só que com as consoantes em maiúsculas
	str -> str"""
    
    consoantes = 'bcdfghjklmnpqrstvwz'
    i = 0
    
    while i < len(frase):
        if frase[i] in consoantes:
            frase = frase.replace(frase[i], frase[i].upper())
        i = i + 1
	return frase