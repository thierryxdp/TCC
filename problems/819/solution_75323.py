def filtra_multiplos(lista,n):
    indice=0
    multiplos=[]
    while indice <len(lista):
        if indice % n:
            multiplos.append(lista[indice])
            indice+=1

        else:
            indice=indice+1
    return multiplos