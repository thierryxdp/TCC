def filtraMultiplos(lista,n):
    '''...'''
    
    multiplos = []
    indice = 0
    
    while indice<=len(lista):
        indice+=1
        if lista[indice]%n==0:
            multiplos+=(lista[indice],)

    return multiplos