def filtraMultiplos(numeros,n):
    '''
       Dada uma lista de números e um número a função retorna
       uma nova lista contento apenas os números da lista
       numeros que são divisíveis por n
       list, int -> list
    '''
    d = n
    while numeros%[d]==0:
        d=d+1
    return d