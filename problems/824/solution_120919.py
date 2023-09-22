def uppCons (frase):
    '''função que recebe como entrada uma frase e retorna a frase com suas consoantes em maiúsculas.
    str -> str'''
    i = 0
    while i > len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyz":
            frase = frase.replace(frase[i],frase[i].upper()
    return frase