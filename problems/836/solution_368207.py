def busca(setor,matriz):
    resultado =[]
    for i in range(0,len(matriz)):
        if matriz[i][2] == setor:
            list.append(resultado,matriz[i])
            del resultado[i][2]
    return resultado