def filtraMultiplos (lista0,n):
    '''função que recebe uma lista e um número 'n' e retorna os números da lista multiplos de 'n'
    list,int->list'''
    i=0
    lista1=[]
    while i < len(lista0):
        if lista0[i]%n==0:
            lista1 = lista1 + [lista0[i],]
            else:
                lista1=lista1
            i=i+1
    return lista1