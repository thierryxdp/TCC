def filtraMultiplos(lista,n):
    '''...'''
    
    multiplos = []
    indice = 3
    
    while indice<=len(lista):
        if lista[indice]%n==0:
            multiplos+=(lista[indice],)
            indice+=1
            return multiplos