def filtraMultiplos(lista,n):
    '''...'''
    
    multiplos = []
    indice = 0
    
    while indice<=len(lista):
        indice+=1
        multiplos+=(lista[indice],)
        if lista[indice]%n==0:
            return multiplos