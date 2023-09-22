def filtraMultiplos(lista,n):
    '''Retorna os números da lista que são divisíveis por n
list,int -> list'''
    i=0
    divisiveis=[]
    while i<len(lista):
        if lista[i]%n==0:
            divisiveis=divisiveis+[lista[i]]
        i=i+1
    return divisiveis