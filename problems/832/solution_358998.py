def eh_quadrada(matriz):
    
    
    n_linha=len(matriz)
    n_coluna=len(matriz[0])
    resultado =[]
        
    for i in range(n_linha):
        linha = n_linha*[0]
        list.append(resultado,linha)
    for i in range(n_linha):
        for j in range(n_coluna):
            resultado[i][j]=matriz[i][j]
    return resultado