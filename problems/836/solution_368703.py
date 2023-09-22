def busca(setor,matriz):
    
    nlinha = len(matriz)
    ncoluna = len(matriz[0])
    resultado = []
    
    for i in range(nlinha):
        if setor == matriz[i][2]:
            resultado += [[matriz[i][0],matriz[i][1],matriz[i][3]]]
            
    return resultado