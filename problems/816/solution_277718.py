def maiores(lista, n):
    """Retorna uma outra lista que contenha apenas os numeros maiores n da lista original
       Entrada: list, int;
       Saida: list;
    """
    lista.append(n)
    lista.sort()
    posicao = lista.index(n)
    return lista[posicao + 1:]