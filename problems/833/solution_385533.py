def conta_numero(numero,matriz):
    """
    	conta quantas vezes o número inserido aparece na matriz
        int, list -> int    	
    """
    qnt_num = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                qnt_num += 1
    return qnt_num