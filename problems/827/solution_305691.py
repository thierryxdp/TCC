def qnd_divisores(n):
    ''' Função que retorna o número de divisores que um dado número n tem
    int -> int '''
    lista = []
    for x, y in range(n+1):
        if x % y == 0:
            list.append(lista, x)
    return len(lista)