def busca(setor,matriz):
    #  lista de strings (matriz) --> lista de strings
    num_linhas = len(matriz)
    lista_saida = []
    for i in range(0,num_linhas):
        if matriz[i][2] == setor:
            listaaux=[matriz[i][0],matriz[i][1],matriz[i][3]]
            lista_saida.append(listaaux)
    return lista_saida