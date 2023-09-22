def uppCons (frase: str)-> str:
    '''Retorna a frase de entrada com todas as consoantes maúsculas'''
    i = 0
    aux = ''
    while i < len(frase):
        if frase[i] in 'aeiou':
            aux = aux + frase[i]
        else:
            aux = aux + frase[i].upper()
        i = i + 1
    return aux