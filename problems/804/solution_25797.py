def filtra_pares(t):
    """função que recebe uma tupla de quatro elementos  inteiros como parâmetro,  e retorna  uma nova tupla contendo  apenas os elementos  pares da tupla original
    tupla -> tupla"""
    lista = []
    if t[0:0] % 2 == 0:
        return lista.append(t[0:0])
    if t[0:1] % 2 == 0:
        return lista.append(t[0:1])
    if t[0:2] % 2 == 0:
        return lista.append(t[0:2])
    if t[0:3] % 2 == 0:
        return lista.append(t[0:3])