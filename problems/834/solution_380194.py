def media_matriz(m):
    """
    Código que retorna média dos números da matriz
    :return ---> list:
    :return --->int:
    """
    acumulas = 0
   
    
    i = 0
    
    for i in range(len(m)):
        
        for j in range(len(m[i])):
                acumulas = acumulas + m[i][j]
    
    numerados = len(m[i]) * len(m)
    divides = acumulas / (len(m[i]) * len(m))
   
    return round(divides, 2)