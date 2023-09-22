def media_matriz(matriz):
    """ """
    l = len(matriz)
    c = len(matriz[0])
    soma = 0
  
    for i in range(l):
        for j in range(c):
            num = matriz[i][j]
            soma = soma + num
            
    return  round((soma/(l*c)),2)