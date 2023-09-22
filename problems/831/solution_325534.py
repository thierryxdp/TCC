def lingua_p(frase):
    ''' função que recebe como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida para a língua do P.
    Entrada: str;
    Saída: str'''
    for índice in range(len(frase)):
        if frase[índice] in 'AEIOUaeiou':
            frase[0:índice+1] + 'p' + frase[índice] + frase[índice + 1: ]
        return frase