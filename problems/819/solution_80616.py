def filtraMultiplos (lista,n):
    '''dada uma lista, retorna uma outra lista com todos os elementos da original que são divisíveis por n'''
    '''list,float->list'''
    
    lista = []
    proximo = 0
    
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            lista = lista + [lista[proximo],]
            proximo = proximo + 1
            return lista