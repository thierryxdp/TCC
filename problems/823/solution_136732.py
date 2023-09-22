def faltante(lista):
    '''Função que dada uma lista com N-1 inteiros enumeados de 1 a N, descobre qual;
    número inteiro deste intervalo está faltando;
    list -> int'''
    i=0
    peca=1
    while i<len(lista):
        if lista[i] in lista:
            i+=1
            peca+=1
        else:
            return peca
    return lista[i]