def filtraMultiplos(lista,numero):
    
    indice=()
    listaN=[]
    
    while indice<len(lista):
        if lista[indice]%numero==0:
            list.append(listaN,lista[indice])
            indice=indice+1
    
    return listaN