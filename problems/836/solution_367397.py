def busca(setor, matriz):
    resultado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor in str(matriz[i][j]):
                resultado += [matriz[i]]
    for i in range(len(resultado)):
        for j in resultado[i]:
            if str(resultado[i][j])==str(setor):
                del resultado[i][j]
    return resultado