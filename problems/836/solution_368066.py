def busca(setor,matriz):
    copiaMatriz = matriz.copy()
    linhas = len(matriz)
    resultado = []
    for i in range(linhas):
        setor1 = matriz[i][2]
        if setor in matriz[i]:
            matriz[i].remove(setor)
            resultado.append(matriz[i])
        else:
            pass
    return resultado