def busca(setor, matriz):
    resultado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor.upper() in str(matriz[i]).upper():
                matriz[i].remove(matriz[i][j])
                resultado += [matriz[i]]
    return resultado