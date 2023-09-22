def filtra_pares(t):
    """função que recebe uma tupla de quatro elementos  inteiros como parâmetro,  e retorna  uma nova tupla contendo  apenas os elementos  pares da tupla original
    tupla -> tupla"""
    lista = []
    if type(t) == tuple and len(t) == 4:
        for i in t:
            if i%2 == 0:
                lista.append(i)
                return (tuple(lista))