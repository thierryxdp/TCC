def lingua_p(frase):
    """ função que recebe como entrada uma frase e retorna a mesma traduzida para a lingua do P, além de retornar a frase em minúsculas;
    str -> str """
    indice = 0
    while indice < (len(frase)):
        if frase[indice] in 'AEIOUaeiouéíáú':
            frase = frase[0:indice+1]
            indice = indice + 2
        indice = indice + 1
    return frase