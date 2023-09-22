def busca(setor, matriz):
    resultado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor in str(matriz[i][j]):
                resultado += [matriz[i]]
                
    for i in range(len(resultado)):
        tam=len(resultado[i])-1
        for j in range(tam):
            if resultado[i][j]== setor:
                del resultado[i][j]
                
    return resultado