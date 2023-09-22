def maiores(lista_numero,n):
    """função que, dados uma lista de número inteiros e um número inteiro 
    n, retorna uma lista contendo apenas os números maiores que n.
    list, int -> list"""
    lista_atual = lista_numero + [n]
    lista_atual.sort()
    x = list.index(lista_atual,n)

    return lista_atual[x+1:]