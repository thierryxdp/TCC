def maiores (lista,n):
    """Função que dada uma lista de inteiros e um inteiro 'n' retorna outra lista que contenha todos os números maiores que 'n' em ordem crescente"""
    """lista, int -> lista"""
    maiores = list()
    lista.sort()
    for c in lista:
        if c >= n:
            maiores.append(c)
    return maiores