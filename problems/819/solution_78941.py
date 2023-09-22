def filtraMultiplos(lista, numero):
    ''' função que recebe uma lista de números e um número n e retorna uma lista com os elementos da lista fornecida que forem divisíveis por n;
	list, int -> list '''
    n_divisiveis = ()
    x = 0
    while x < len(lista):
        if lista[x]%numero == 0:
            n_divisiveis = n_divisiveis + (lista[x], )
        x = x + 1
    return list(n_divisiveis)