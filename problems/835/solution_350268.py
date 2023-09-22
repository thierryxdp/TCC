def melhor_volta(m):
    ''' '''
    '''list(list) -> tuple'''
    
    volta = []
    tempos_min = []
    
    for listas in m:
        tempos_min += [min(listas),]
        
    menor_tempo = min(tempos_min)
    corredor = list.index(tempos_min,menor_tempo)+1
    
    for listas in m:
        for j in listas:
            if j == menor_tempo:
                melhor_volta = list.index(listas,j)+1
      
    return (corredor, menor_tempo, melhor_volta)