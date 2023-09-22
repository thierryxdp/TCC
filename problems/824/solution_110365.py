uppCons(frase):
    '''retorna uma frase com todas as consoantes maisculas
    str -> str'''
    i=0
    vogais = ['aeiouAEIOU']
    
    while i < len(frase):
        if (frase[i] not in vogais):
            frase[i].upper()
        i = i + 1
    return frase