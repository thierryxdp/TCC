def filtraMultiplos(lista,n):
    ''' Funcao que retorna os multiplos de uma lista;
    list->list'''
    mult=[]
    prox=0
    while prox<len(lista):
        if lista[prox]%n==0:
            mult=mult+(lista[prox],)
        prox = prox+1
    return mult