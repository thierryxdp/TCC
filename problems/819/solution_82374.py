def filtraMultiplos(lista,n):
    '''
    função que dada uma lista e um inteiro retorna os números da lista que são divisiveis por n
    list,int-->list    
    '''

    divisiveis=[]
    i=0

    while i<len(lista):
        if lista[i]%n==0:
            divisiveis= divisiveis + [lista[i]]
        i = i+1

    return divisiveis