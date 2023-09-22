def insere(a,b):
    """Função que insere um número em uma lista em sua posição correta seguindo uma ordem crescente de valor;
    list, int -> list"""
    a += [b]
    list.sort(a)
    return a