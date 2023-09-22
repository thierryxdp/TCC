def busca(setor, matriz):
    resultado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor in str(matriz[i][j]):
                resultado += [matriz[i]]
    resultado = numpy.delete(resultado,(2), axis=1)
    return resultado