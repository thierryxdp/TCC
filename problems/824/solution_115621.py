def uppCons(frase):
    """Recebe uma frase e retorna a mesma com todas as consoantes maiusculas.
    	str -> str"""
    frase = list(frase)
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
            frase[i] = frase[i].upper()
        i += 1
    frase = "".join(frase)
    return frase