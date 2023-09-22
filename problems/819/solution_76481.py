def filtraMultiplos(lista, n):
    '''função que, dado uma lista e um numero n (int), retorna quais elementos
    da lista são multiplos de n'''
    newList = []
    cont = 0
    
    while(cont < len(lista)):
        if lista[cont] % n == 0:
            newList.append(lista[cont])
            
        cont = cont + 1
            
    
    return newList