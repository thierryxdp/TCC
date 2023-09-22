def maiores(lista,n):
    """Funcao que dada uma lista de numeros inteiros e um numero 
    inteiro n, retorna outra lista que contem os numeros da lista
    original maiores que esse numero n; list,int->list"""
    lista.append(n)
    lista.sort()
    indice=lista.index(n)
    return lista[indice+1:]