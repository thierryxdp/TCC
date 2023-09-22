def uppCons(frase):
    '''recebe uma frase e retorna ela com as consoantes em maiusculas
    str -> str'''
    indice = 0
    a = frase[indice] 
    while indice < len(frase):
        if frase[indice] not in "aeiouAEIOUáéíóúãÁÉÍÓÚÃ":
            frase = frase[:indice-1] + str.upper(frase[indice]) 
        indice = indice + 1
    return frase