def filtraMultiplos(lista,numero):
    multiplos=[]
    indice=0
    while indice<=len(lista):
        if lista[indice]%numero==0:
            multiplos=multiplos+[lista[indice]]
        indice=indice+1
    return multiplos