def uppCons(frase):
    '''recebe uma frase e retorna ela com as consoantes em maiusculas
    str -> str'''
    indice = 0
    while indice < len(frase):
        if frase[indice] not in "aeiouAEIOU":
            str.upper(indice)
        indice = indice + 1
    return frase