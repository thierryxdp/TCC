def busca(setor,matriz):
    '''Função que, dados um setor de uma empresa e uma matriz de 4 colunas, retorna as informações sobre cada integrante daquele setor da empresa.
str,list(list) --> list(list)'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    lista_final = []
    for i in range(linhas):
        if matriz[i][2] == setor:
            lista_final = lista_final + [[matriz[i][0],matriz[i][1],matriz[i][3]]]
    return lista_final