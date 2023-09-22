def lingua_p(frase):
    ''' função que recebe como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida para a língua do P.
    Entrada: str;
    Saída: str'''
    for indice in range(len(frase)):
        if frase[indice] in 'AEIOUaeiou':
            frase[0:indice+1] + 'p' + frase[indice] + frase[indice + 1: ]
        return frase