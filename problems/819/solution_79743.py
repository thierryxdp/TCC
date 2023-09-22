def filtraMultiplos(lista,n):
    '''...'''
    
    indice = 0
    multiplos = []
    
    
    while indice<=len(lista):
        if lista[indice]%n==0:
            list.append(multiplos,indice)
            multiplos+=1
            return multiplos