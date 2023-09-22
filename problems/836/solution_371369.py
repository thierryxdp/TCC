def busca(setor,matriz):
    #  lista de strings (matriz) --> lista de strings
    num_linhas = len(matriz)
    lista_saida = []
    for i in range(0,num_linhas):
        if matriz[i][2] == setor:
            lista_saida.append(matriz[i])
    return lista_saida