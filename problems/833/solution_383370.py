def conta_numero(numero, matriz):
    """Retorna quantas vezes aquele numero aparece na matriz, dados:
    um numero inteiro e uma matriz."""
    
    ap = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                ap = ap+1
                
    return ap