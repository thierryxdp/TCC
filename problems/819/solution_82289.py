def filtraMultiplos(lista, numero):
    indice=0
    multiplos=[]
    while indice < len(lista):
        if lista[indice]%numero==0:
            list.append(multiplos, lista[indice])
        indice = indice + 1
    return multiplos