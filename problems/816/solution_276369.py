def maiores(lista, n):
    """Função que dada uma lista de números e um inteiro 'n', retorna uma lista  com todos
    os números maiores que 'n';
    list, int -> list"""
    lista.append(n)
    lista.sort()
    p = lista.index(n)
    return lista[p+1:]