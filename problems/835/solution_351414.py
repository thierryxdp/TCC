def melhor_volta(matriz):
    numero_volta=0
    cada_corredor=0
    total_corredor=[]
    total_volta=[]
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j]<=matriz[j][i]:
                cada_corredor=matriz[i][j]
                numero_volta=j+1
        list.append(total_corredor,cada_corredor)
        list.append(total_volta,numero_volta)
        
    for l in range(5):
    for c in range(1,6):
        if total_corredor[l]<=total_corredor[c]:
            tempo=total_corredor[l]
            vencedor=l+1
            indice=l
    volta=total_volta[indice]+1    
    mehor=melhor+(vencedor,tempo,volta,)
    #mehor=melhor+(vencedor,)
    return melhor