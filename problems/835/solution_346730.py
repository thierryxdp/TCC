def melhor_volta(m):
    '''Função que dada uma matriz retorna o menor valor encontrado, a
    linha em que foi encontrado e o valor em si. list -> tuple'''
    i = 1
    j = 1
    while i <= len(m):
        while j <= len(m[i]):
            if m[i][j] == min(m[i]):
                x = i
                y = m[i][j]
                z = j
            else:
                j = j + 1
            j = j + 1
        i = i + 1
    return (x, y, z)