def filtraMultiplos(lista,n):
    '''...'''
    
    multiplos = []
    indice = 0
    
    while indice<=len(lista):
        indice+=1
        if lista[indice]%n==0:
            indice+=1
            multiplos+=(lista[indice],)
            
    return multiplos