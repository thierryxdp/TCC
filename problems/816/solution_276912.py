def maiores(lista,n):
    """funcao que retorna uma lista com numeros maiores dado um numero em relacao a uma lista;
    list,int -> list"""

    if n in lista:
        lista.sort()
        posicao = lista.index(n)
        return lista[posicao+1:]

    else:
        lista.append(n)
        lista.sort()
        posicao = lista.index(n)
        return lista[posicao+1:]