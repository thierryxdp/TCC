def filtraMultiplos(lista,n):
    """Recebe uma lista com números e um número n que se deseja saber quantos números da lista são múltiplos desse número n, devolvendo uma lista com esses números;
    	list, int -> list"""
    indice=0
    listaresposta=[]
    parada=len(lista)-1
    while indice<=parada:
        if lista[indice]%n==0:
            list.append(listaresposta,lista[i])
        indice=indice+1
    return listaresposta