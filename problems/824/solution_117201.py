def uppCons(frase):
    '''Função que dada uma frase qualquer, retornará todas as consoantes da frase em maiúsculo,
    e os demais caracteres sem alteração.
    frase - > str
    return -> str'''
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    i = 0
    fraseMaius = frase
    while i < len(frase):
        if frase[i] in consoantes:
            fraseMaius[i].upper()
        i+= 1