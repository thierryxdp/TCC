def filtraMultiplos(lista,n):
    '''Recebe uma lista de numeros e um numero.
    retorna os elementos da lista divisiveis pele numero.
    list,int->list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n==0:
            multiplos = multiplos +[lista[i]]
        i=i+1
    return multiplos