def faltante(lista):
    '''Função que dada uma lista com N-1 inteiros enumeados de 1 a N, descobre qual;
    número inteiro deste intervalo está faltando;
    list -> int'''
    i=0
    lnumeros = [1,2,3,4,5,6,7,8]
    while i<=len(lista):
        if lista[i]!=lnumeros:
            faltante = lista[i]
    return faltante