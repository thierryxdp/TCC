def melhor_volta(matriz):
    '''Essa função ao receber uma matriz 6x10 com os tempos em segundos do corredores em cada volta.A função retorna uma tupla informando:De quem foi a melhor volta da prova, com qual tempo e em que volta'''
    '''list(list) -> tuple'''
    
    volta = []
    tempos_min = []
    
    for listas in matriz:
        tempos_min += [min(listas),]
        
    menor_t = min(tempos_min)
    corredor = list.index(tempos_min,menor_t)+1
    
    for listas in matriz:
        for j in listas:
            if j == menor_t:
                melhor_volta = list.index(listas,j)+1
      
    return (corredor, menor_t, melhor_volta)