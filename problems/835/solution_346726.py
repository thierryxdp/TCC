def melhor_volta(m):
    '''Função que dada uma matriz retorna o menor valor encontrado, a
    linha em que foi encontrado e o valor em si. list -> tuple'''
    tupla = ()
    for i in range(0, 6):
        tupla += min(m[i])
    x = min(tupla)
    y = list.index(m[i], x)
    result = (m[i], x, y)
    return result