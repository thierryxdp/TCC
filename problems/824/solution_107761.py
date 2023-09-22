def uppCons(frase):
    ''' Funcao que recebe como entrada uma frase
    e retorna a mesma frase com todas as consoantes maiusculas'''
    i=0
    while i<=len(frase):
        if frase[i] not in'AEIOUaeiou':
            frase[i]=frase.upper()
        i=i+1
    return frase