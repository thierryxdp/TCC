def maiores(lista,n):
    """Função que ao receber uma lista de números inteiros e um número
    inteiro, retorna outra lista que contenha apenas os números originais,
    maiores que o número dado;
    list, int -> list"""
    lista[0:0] = [n]
    list.sort(lista)
    x = list.index(lista,n)
    return lista[x+1:]