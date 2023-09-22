def uppCons(frase):
    '''recebe uma frase e retorna ela com as consoantes em maiusculas
    str -> str'''
    indice = 0
    while indice < len(frase):
        if frase[indice] not in "aeiouAEIOU":
            frase = frase[:indice - 1] + str.upper(frase[indice]) 
        indice = indice + 1
    return frase