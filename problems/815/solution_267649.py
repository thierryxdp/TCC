def insere(lista, n):
    """Função que dada uma lista de números em ordem crescente e um inteiro 'n', o insere
    na posição correta de modo que a lista continua ordenada;
    list, int -> list"""
    lista.append(n)
    lista.sort()
    return lista