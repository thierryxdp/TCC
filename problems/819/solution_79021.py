def filtraMultiplos(lista,n):
    
    """Função que filtra os múltiplos de um número n"""
    
    indice=0
    multiplos=[]
    s=0
    while (indice<len(lista)):
        if (lista[indice] % n) == 0:
            s=s+lista[indice]
            list.append(multiplos, lista[indice])
        indice=indice+1
    return multiplos