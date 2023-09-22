def uppCons(frase):
    '''função que rebe de entrada uma frase e retorna a mesma
    frase com as consoantes maiusculas. str -> str'''
    fraseN = ''
    i=0
    fraseN = ''
    i=0
    consoantes= 'bBcCçÇdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ'
    while i<len(frase):
        if frase[i] in consoantes:
            fraseN = fraseN + str.upper(frase[i])
            i=i+1
        elif frase[i] not in consoantes:
            fraseN = fraseN + frase[i]
            i=i+1
    return fraseN