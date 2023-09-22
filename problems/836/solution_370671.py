def busca(matriz,setor):
    ''' função que dado uma matriz e um setor, retorna os dados
    de todos os funcionários daquele setor. list, string -> list'''
    r = []
    for a in range (len(matriz)):
        for b in range (len(matriz[a])):
            if matriz[a][b] == setor:
                p = [matriz[a][0],matriz[a][1],matriz[a][3]]
                list.append(r,p)
    return r