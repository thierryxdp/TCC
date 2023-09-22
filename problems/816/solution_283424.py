def maiores(lista,n):
    '''função que retorna uma lista em ordem crescente
    dos números maiores que n
    valor de entrada: list, int
    valor de saída: list'''
    lista.append(n)
    lista.sort()
    crescente= lista[lista.index(n)+1:]
    arrumada= crescente.sort()
    return arrumada