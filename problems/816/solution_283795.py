def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista = lista + [n]
    nova = list.sort(lista)
    ind = list.index(lista,n)
    maior = lista[ind+1:]
    return maior