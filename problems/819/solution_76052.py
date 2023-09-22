def filtraMultiplos(lista,n):
    indice=0
    multiplos=[]
    while indice<len(lista):
        if lista[indice]%n==0:
            multiplos=multiplos+lista[indice]
            indice=indice+1
        else:
            pass
    return multiplos