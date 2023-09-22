def busca(setor,matriz):
    
    F = []
    
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            F.append(i)
    
    F_final = []
    
    for j in F:
        F_final.append(matriz[j])
    return F_final