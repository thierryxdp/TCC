def uppCons(frase):
    """Recebe uma frase e retorna a mesma com todas as consoantes maiusculas.
    	str -> str"""
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            frase[i] = frase[i].upper()
        i += 1
    return frase