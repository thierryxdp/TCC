def maiores(lista, n):
    """Esta função retorna todos os valores maiores que N da lista
    assinatura: list int ->list
    """
    list(lista)
    lista.append(n)
    ordem = sorted(lista)
    indN = ordem.index(n)
    if n not in ordem:
        lista.append(n)

    return ordem[indN + 1:]