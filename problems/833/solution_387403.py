def conta_numero(numero,matriz):
    """Essa função conta quantas vezes um numero se repete em uma matriz
    int,lista->int"""
    
    contador = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                contador += 1
        
    return contador