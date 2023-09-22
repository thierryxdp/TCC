def posLetra(string,letra,n):
    '''funcao que retorna em qual posicao da frase a letra se repete em relacao ao numero dado
    str,str,int->int'''
    i=0
    acumulador=0
    while n<len(string):
        if string[i] == letra:
            acumulador=acumulador+1
        if acumulador==n:
            acumulador=acumulador+1
            return acumulador
        if acumulador<n:
            return -1