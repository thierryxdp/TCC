def filtra_pares(t):
    """função que recebe uma tupla de quatro elementos  inteiros como parâmetro,  e retorna  uma nova tupla contendo  apenas os elementos  pares da tupla original
    tupla -> tupla"""
    lista2 = sorted(filter(lambda x: x % 2 == 0, t))