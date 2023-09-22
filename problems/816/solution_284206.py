def maiores(lista,n):
    """Dada uma lista de números inteiros e um número inteiro 'n', retorna outra lista contendo
    todos os números maiores que 'n' na lista original, ordenados em ordem crescente; tuple or 
    list, int -> list"""
    lista = list(lista)
    lista.sort()
    if lista[0] <= n:
        for tamanho in range(len(lista)):
            if lista[0] <= n:
                del(lista[0])
    return lista