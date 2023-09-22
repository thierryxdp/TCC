def posLetra(string, letra, n):
    '''Função que dada uma string, uma letra e o número de ocorrências
    retorna o índice em que dada ocorrência se encontra. str, str, int
    -> int'''
    while n < str.count(string, letra):
        x = str.index(string, letra, n)
        return x
    return str.index(string, letra, n)