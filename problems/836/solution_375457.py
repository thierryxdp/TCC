def busca(matriz):
    for i in range(1,len(matriz)): 
        x=matriz[i] 
        j=i-1
        while j>=0 and x<matriz[j]: 
            matriz[j+1]=matriz[j] 
            j==j-1
        matriz[j+1]=x
    return matriz