def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista1 = lista.sort()
    if lista1.find(n) != 0:
        return lista1[n+1:]
    else:
        return 0