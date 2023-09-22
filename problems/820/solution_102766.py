def posLetra(frase, letra, numero):
    '''função que recebe uma frase, uma letra e um número correspondente ao número de 
    ocorrências da letra na frase dada e retorna em qual posição da frase aquela ocorrência 
    da letra se encontra
    str, str, int -> int'''
    x = 0
    z = 0
    while x < len(frase) and x < numero:
        if frase[x] == letra:
            z = z +1
        x = x + 1
    if z < numero:
        return -1
    else:
        return x-1