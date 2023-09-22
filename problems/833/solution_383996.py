def conta_numero(numero, matriz):
    """Funcao que conta quantas vezes o numero fornecido aparece dentro da matriz fornecida;
    int, list(list) -> int"""
    
    contador = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                contador += 1
    return contador