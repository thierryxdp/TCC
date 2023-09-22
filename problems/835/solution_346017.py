def melhor_volta(matriz):
    
    resultado = matriz
    for i in range(6):
        matriz[i] == min(matriz[i])
    
    volta=[]
    corredor=[]
    for j in range(6):
        for k in range(10):
        	if resultado[j][k] == matriz[0]:
                       corredor.append(j)
                       volta.append(k)
    
    tupla = (corredor,matriz,volta)
    return tupla