def filtraMultiplos(lista,numero):
    '''Dado uma lista contendo numeros e um numero qualquer, cria uma nova lista
    contendo todos os elementos originais da primeira lista que forem divisíveis
    por n.list,int->list'''
    a=[]
    b=0
    while b<len(lista):
        if lista[b]%numero==0:
            a.append(lista[b])
        b=b+1
    return a