def busca(setor,matriz):
    resultado = []
    for i in range(len(matriz)):
            if (setor == matriz[i][2]):
                resultado.append(matriz[i])
    return resultado