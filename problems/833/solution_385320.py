def conta_numero(numero, matriz):
    """Recebe um número e uma matriz, e retorna quantas vezes aparece o numero na matriz
    	int, list -> int"""
    count = 0
    
    for i in matriz:
        for j in matriz[i]:
            if matriz[i][j] == numero:
                count += 1
    
    return count