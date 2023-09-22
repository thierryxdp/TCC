def media_matriz(matriz):
    """ Esta função calcula a média entre as matrizes
    dict -> float """
    x = []
    for i in range(len(matriz)):
        x.append(matriz[i])	
        if x == len(matriz):
             
            print  sum(x)/len(x)