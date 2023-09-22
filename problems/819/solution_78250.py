def filtraMultiplos(lista,n):
    '''função que dada uma lista de numeros e um numero,
    retorna uma lista com os divisiveis por n
    list,int-> list'''
    lista1=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            list.append(lista1,lista[i])
        i=i+1
    return lista1