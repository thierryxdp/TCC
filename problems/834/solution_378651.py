def media_matriz(matriz):
    """
    	Calcula a media dos inteiros de determinada matriz
        list -> float    	
    """
    soma_nums=0
    qnt_nums=0
    for i in len(matriz):
        for j in len(matriz[0]):
            soma_nums += matriz[i][j]
            qnt_nums += 1
    media = soma_nums/qnt_nums
    return media