def filtraMultiplos(lista, numero):
    """Função que retorna uma lista com elementos de uma lista recebida que são divisiveis por n
    list, int-> list"""
    n_divisiveis = ()
    x = 0
    while x < len(lista):
        if lista[x]%numero == 0:
            n_divisiveis = n_divisiveis + (lista[x], )
        x = x + 1 
    return list(n_divisiveis)