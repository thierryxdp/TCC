def busca(setor, matriz):
    resultado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor.upper() in str(matriz[i][j]).upper():
                resultado += [lista[i][j]]
    return resultado