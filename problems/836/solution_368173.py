def b(setor,matriz):
    resultado =[]
    for i in range(0,len(matriz)):
        if matriz[i][2] == setor:
            del matriz[i][2]
            list.append(resultado,matriz[i])
    return resultado