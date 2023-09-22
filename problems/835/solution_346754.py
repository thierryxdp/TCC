def melhor_volta(m):
    '''Função que dada uma matriz retorna o menor valor encontrado, a
    linha em que foi encontrado e o valor em si. list -> tuple'''
    i = 0
    j = 0
    while i <= len(m):
        while j <= 9:
            if m[i][j] == min(m[i]):
                    y = m[i][j]
                    z = j
                    x = i
        j = j + 1
        i = i + 1
    return (x, y, z)