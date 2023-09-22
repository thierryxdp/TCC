def conta_numero(numero,matriz):
    """Funcao que retorna quantas vezes o numero irá aparecer na matriz"""
    count = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                count += 1
    return count