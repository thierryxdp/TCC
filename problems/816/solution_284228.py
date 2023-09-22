def maiores(lista,n):
    insere(lista,n)
    indice=list.index(lista,n)
    maior=indice+1
    return lista[maior:]