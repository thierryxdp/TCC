def melhor_volta(matriz):
    tempos=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            tempos+=[matriz[i][j]]
            
    
    corredor_menor_volta=((tempos.index(min(tempos)))//10)+1
    volta=tempos.index(min(tempos))+1
    
    return corredor_menor_volta,tempos.index(min(tempos)),volta