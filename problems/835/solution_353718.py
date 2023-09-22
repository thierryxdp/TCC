def melhor_volta(matriz):
    '''retorna de quem foi a melhor volta, 
    com qual tempo e em que volta; entrada-> matriz 6x10;
    list(mat)-> tupla'''
    menor=100
    vl=False
    i=0
    j=0
    for linha in matriz:
        for elem in linha:
            if elem <= menor:
                menor = elem
    while vl=False: 
    	if matriz[i][j]== menor:
            i=i
            j=j
            vl=True
        i=i+1
        j=j+1
        
    tupla=(i, menor,j)        
    
    return tupla