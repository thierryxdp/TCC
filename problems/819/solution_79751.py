def filtraMultiplos(lista,n):
    '''...'''
    
    multiplos = []
    indice = 0
    
    while indice<=len(lista):
        if lista[indice]%n==0:
            list.append(multiplos,indice)
            multiplos+=(n[indice],)
            indice+=1
            return multiplos