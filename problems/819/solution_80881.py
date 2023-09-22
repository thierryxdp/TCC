def filtraMultiplos (lista,n):
    '''dada uma lista, retorna uma outra lista com todos os elementos da original que são divisíveis por n'''
    '''list,float->list'''
    
    listanv = []
    proximo = 0
    
    while proximo <len(lista):
        if lista[proximo] %n == 0:
            listanv = listanv + [lista[proximo]]
            proximo = proximo + 1
            return listanv