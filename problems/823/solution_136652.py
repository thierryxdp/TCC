def faltante(lista):
    '''Função que dada uma lista com N-1 inteiros enumeados de 1 a N, descobre qual;
    número inteiro deste intervalo está faltando;
    list -> int'''
    i=0
    pa = n*(1+n)/2
    peca='' 
    while i<=len(lista):
        if lista[i]==pa:
          peca = peca+1
    return peca