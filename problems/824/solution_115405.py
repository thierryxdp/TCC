def uppCons(frase):
    """funcao que recebe uma frase e retorna a mesma só que com todas as consoantes em maiúsculas
	str -> str"""
    
    maius = 'bcçdfghjklmnpqrstvwyz'
    i = 0
    
    while len(frase) > i:
        if frase[i] in maius:
            frase = frase.replace(frase[i], frase[i].upper())
        i = i + 1 
    
    return frase