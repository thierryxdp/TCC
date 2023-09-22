def maiores(lista,n):
    '''função que retorna uma lista em ordem crescente
    dos números maiores que n
    valor de entrada: list, int
    valor de saída: list'''
    list.insert(lista,n)
    lista.sort()
    maiores= lista[lista.index(n)+1:]
    return maiores.sort()