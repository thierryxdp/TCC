def uppCons(frase):
    '''Retorna a frase de entrada com as consoantes maiúsculas
    	str -> str'''
    i = 0
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU':
            frase = frase[:i] + str.upper(frase[i])
        else:
            frase = frase
    	i = i + 1
    return frase