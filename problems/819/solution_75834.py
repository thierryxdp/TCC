def filtraMultiplos(lista,numero):
    '''dada uma lista de números e um número, retorna todos os elementos da lista que são divisíveis por numero;
    list, int --> list'''
    prox=0
    listaa=[]
    while prox<len(lista):
        if lista[prox]%numero==0:
            listaa=listaa+[lista[prox]]
        prox=prox+1
    return listaa