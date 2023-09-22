def uppCons(frase):
    '''dada uma frase (frase), retorna a mesma frase com todas as consoantes maiusculas; str -> str'''
    indice  = 0
    frase2 = ''
    while indice < len(frase):
        if frase[indice] not in ('AEIOUaeiou'):
            frase2 = frase2 + str.upper(frase[indice])
        else:
            frase2 = frase2 + frase[indice]
        indice = indice + 1
    return frase2