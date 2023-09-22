def busca(setor,matriz):
    resultado=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            resultado+=[[matriz[i][0],matriz[i][1],matriz[i][3]]]
    return resultado