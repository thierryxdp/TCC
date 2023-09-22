def maiores(lista,n):
    """recebe uma lista de numeros inteiros e um numero n e retorna todods os numeros
da lista maiores que n.
lista,int->lista"""
    list.append(lista,n)
    list.sort(lista)
    indice=list.index(lista,n)
    if lista[indice]!=lista[indice+1]:
        return lista[indice+1:]
    elif lista[indice]==lista[indice+1]:
        return lista[indice+2:]