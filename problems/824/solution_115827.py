def uppCons(frase):
    '''Dado uma frase, retornará a mesma frase com as consoantes maiusculas.
    (str => str)'''

    fraseN = ''
    i = 0
    consoantes = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVxXyYwWzZ'

    while i < len(frase):
        if frase[i] in consoantes:
            fraseN = fraseN + str.upper(frase[i])
            i = i + 1
            
        elif frase[i] not in consoantes:
            fraseN = fraseN + frase[i]
            i = i + 1
            
    return fraseN