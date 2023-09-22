def posLetra(string, letra, n):
    '''Função que dada uma string, uma letra e o número de ocorrências
    retorna o índice em que dada ocorrência se encontra. str, str, int
    -> int'''
    i = 0
    acumulador = 0
    while acumulador <= n:
        if acumulador < n:
            acumulador = acumulador + str.count(string, letra, n)
        x = str.index(string, letra)
    if n > str.count(string, letra, n):
        return -1
    return x