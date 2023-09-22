def conta_numero(numero,matriz):
    """Retorna a quantidade de vezes que o número de entrada aparece na matriz.
    int, lista --> int"""
    
    quantidade = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(quantidade,matriz[i][j])
            
    return list.count(quantidade,numero)