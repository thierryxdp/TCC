def filtraMultiplos(lista,numero):
    indice=0
    while lista[indice]%numero==0:
        indice=indice+1
        lista=lista + lista[indice]
    return lista