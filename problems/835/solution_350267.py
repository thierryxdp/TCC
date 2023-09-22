def melhor_volta(m):
    '''list(list) -> tuple'''
    
    voltas = []
    tempos_min = []
    
    for i in m:
        tempos_min += [min(i),]
        
    menor_tempo = min(tempos_min)
    corredor = list.index(tempos_min,menor_tempo)+1
    
    for i in m:
        for j in i:
            if j == menor_tempo:
                melhor_volta = list.index(i,j)+1
      
    return (corredor, menor_tempo, melhor_volta)