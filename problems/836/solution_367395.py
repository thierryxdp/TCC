def busca(setor, matriz):
    resultado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor in str(matriz[i][j]):
                resultado += [matriz[i]]
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            if setor == resultado[i][j]:
                del resultado[i][j]
    return resultado