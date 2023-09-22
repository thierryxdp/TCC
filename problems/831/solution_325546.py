def lingua_p(frase):
    ''' função que recebe como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida para a língua do P.
    Entrada: str;
    Saída: str'''
    indice = 0
    while indice < (len(frase)):
        if frase[indice] in 'AEIOUaeiouéíáú':
            frase = frase[0:indice+1] + 'p' + frase[indice] + frase[indice + 1: ]
            indice = indice + 2
        indice = indice + 1    
    return frase