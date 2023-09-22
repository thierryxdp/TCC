def busca(setor,matriz):
    
    F = []
    
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            F.append(i)
    
    F_meio = []
    F_final = []
    
    for j in F:
    
    	F_meio.append(matriz[j][0])
        F_meio.append(matriz[j][1])
        F_meio.append(matriz[j][3])
        
        F_final.append(F_meio)
        F_meio = []
    
    return F_final