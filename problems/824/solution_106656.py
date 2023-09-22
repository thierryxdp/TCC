def uppCons(frase):
    '''recebe uma frase e retorna ela com as consoantes em maiusculas
    str -> str'''
    indice = 0
    a = frase[indice] 
    while indice < len(frase):
        if frase[indice] not in "aeiouAEIOUáéíóúãÁÉÍÓÚÃ":
            str.upper(frase[indice]) = x
            str.replace(frase, indice, x)
        indice = indice + 1
    return frase