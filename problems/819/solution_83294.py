filtraMultiplos(lista,n):
    '''
    Recebe uma lista de inteiros e um inteiro n e retorna os elementos de lista
    divisiveis por n
    list, int-> list
    '''
    mult=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            mult=mult+[lista[i]]
        i=i+1
    return mult