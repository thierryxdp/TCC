def melhor_volta(matriz):
    melhor=()
    numero_volta=0
    cada_corredor=0
    total_corredor=[]
    total_volta=[]
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(linha-1):
             if matriz[j+1][i]>=matriz[j][i]:
                cada_corredor=matriz[j][i]
                numero_volta=j
            if matriz[j+1][i]<=matriz[j][i]:
                cada_corredor=matriz[j+1][i]
                numero_volta=j+1    
        list.append(total_corredor,cada_corredor)
        list.append(total_volta,numero_volta)
        
    vencedor=min(total_corredor)
    indice=list.index(total_corredor,vencedor)
    melhor=melhor+(indice+1,total_corredor[indice],total_volta[indice]+1,)
    return melhor