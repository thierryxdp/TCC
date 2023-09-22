def posLetra(string, letra, n):
    '''Função que dada uma string, uma letra e o número de ocorrências
    retorna o índice em que dada ocorrência se encontra. str, str, int
    -> int'''
    i = 0
    acumulador = 0
    x = 0
    while acumulador < n and  i <= len(string):
        if string[i] == letra:
            acumulador = acumulador + 1
            x = i
        i = i + 1
    if acumulador < n:
        return -1
    else:
        return x