def posLetra(string, letra, n):
    '''Função que dada uma string, uma letra e o número de ocorrências
    retorna o índice em que dada ocorrência se encontra. str, str, int
    -> int'''
    while n <= str.count(string, letra):
        x = str.index(string, letra, n)
        return x
    if n > str.count(string, letra):
        return -1
    if n > 2:
        return str.index(string, letra, n + 1)