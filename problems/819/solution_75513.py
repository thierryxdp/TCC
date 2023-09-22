def filtraMultiplos(lista,numero):
    indice=0
    proximo=0
    lista2=[]
    while proximo<len(lista):
        if (lista[indice])%numero==0:
            indice=indice+1
            proximo=proximo +1
    return lista2