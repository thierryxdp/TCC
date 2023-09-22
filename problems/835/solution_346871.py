def melhor_volta(matriz):
    
    menorReal = 1000
    corredor = 0
    for indice in range(len(matriz)):
        
        menor = min(matriz[indice])
        pos = list.index(matriz[indice], menor)
        if menor < menorReal:
            menorReal = menor
            corredor = indice + 1
            volta = pos + 1
        
        else:
            pass
    resultado = (corredor, menorReal, volta)
    return resultado