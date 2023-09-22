def uppCons (frase: str)-> str:
    '''Retorna a frase de entrada com todas as consoantes maúsculas'''
    i = 0
    aux = ''
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            aux = aux + frase[i].upper()
        else:
            aux = aux + frase[i]
        i = i + 1
    return aux