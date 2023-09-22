def filtraMultiplos(lista, n):
    ''' Essa função filtra os multiplos de um número n, retornando os numeros de dentro da lista que são divisives po n; list,int->list'''
    i=0
    lista1=[]
    while  i<len lista:
        if lista[i]%n==0:
            i=i+1
    return lista1