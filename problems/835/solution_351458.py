def melhor_volta(matriz):
    melhor=()
    vencedor_total_volta=[]
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        vencedor_cada_volta=min(matriz[i])
        list.append(vencedor_total_volta,vencedor_cada_volta)
    vencedor=min(vencedor_total_volta)
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j]==vencedor:
                corredor=j+1
                volta=i+1
    melhor=melhor+(corredor,vencedor,volta,)
    return melhor