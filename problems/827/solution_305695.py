def qtd_divisores(n):
    ''' Função que retorna o número de divisores que um dado número n tem
    int -> int '''
    lista = []
    for x and y in list.range(n):
        if x % y == 0:
            list.append(lista, x)
    return len(lista)