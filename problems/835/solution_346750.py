def melhor_volta(m):
    '''Função que dada uma matriz retorna o menor valor encontrado, a
    linha em que foi encontrado e o valor em si. list -> tuple'''
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == min(m[i]) and m[i] == min(m):
                    y = m[i][j]
                    z = j
                    x = i
    return (x, y, z)