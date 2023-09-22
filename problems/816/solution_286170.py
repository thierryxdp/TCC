def maiores(lista_numero,n):
    """Funçao que dada uma lista de numeros inteiros e um numero inteiro(n),
    retorna outra lista, contendo todos os numeros da lista original
    maiores que n, em ordem crescente"""
    list.append(lista_numero,n)
    lista_numero2 = lista_numero [:]
    list.sort(lista_numero2)
    if (lista_numero2[0]) > n:
        del lista_numero2[0]
        return lista_numero2
    elif lista_numero2[1] > n:
        del lista_numero2[1]
        return lista_numero2
    elif lista_numero2[2] > n:
        del lista_numero2[2]
        return lista_numero2