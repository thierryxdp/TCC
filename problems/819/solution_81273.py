def filtraMultiplos(lista,n):
    '''função que pega os elementos de uma lista, lista, que são múltiplos logo divisíveis pelo número escolhido,n'''
    mult=[]
    prox=0
    while prox<len(lista):
        if lista[prox]%n==0:
            mult=mult+lista[prox]
        prox=prox+1
    return mult