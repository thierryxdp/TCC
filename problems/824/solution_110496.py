def uppCons(frase):
    '''função que rebe de entrada uma frase e retorna a mesma
    frase com as consoantes maiusculas. str -> str'''
    fraseN = ''
    i=0
    while i<len(frase):
        if frase[i] in 'AEIOUaeiou':
            fraseN = fraseN + frase[i]
            i=i+1
        elif frase[i] not in 'AEIOUaeiou':
            fraseN = fraseN + str.upper(frase[i])
            i=i+1
    return fraseN