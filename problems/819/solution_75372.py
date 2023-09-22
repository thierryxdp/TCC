def filtraMultiplos(lista,n):
    indice=0
    multiplos=[]
    while indice <len(lista):
        if lista[indice] % n == 0:
            multiplos.append(lista[indice])
            indice+=1

        else:
            indice=indice+1
    return multiplos