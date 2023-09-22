def melhor_volta(m):
    ''''''
    '''list(list) -> tuple'''
    
    volta = []
    tempos_min = []
    
    for listas in m:
        tempos_min += [min(listas),]
        
    menor_t = min(tempos_min)
    corredor = list.index(tempos_min,menor_t)+1
    
    for listas in m:
        for j in listas:
            if j == menor_t:
                
melhor_volta = list.index(listas,j)+1
      
    return (corredor, menor_t, melhor_volta)