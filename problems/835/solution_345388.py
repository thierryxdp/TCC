def melhor_volta(matriz):
    
    tempos=[]
    for i range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(tempos,matriz[i][j])
    
    Vrapida=min(tempos)
    corredor=list.index(matriz,Vrapida)
    
    return (corredor,Vrapida)