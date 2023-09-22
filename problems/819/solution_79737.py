def filtraMultiplos(lista,n):
    '''...'''
    
    indice = 0
    multiplos = []
    
    
    while indice<=len(lista):
        if lista[indice]%n==0:
            indice+=1
            return multiplos