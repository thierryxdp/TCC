def melhor_volta(m):
    '''recebe como entrada uma matriz 6 x 10, onde são
    6 corredores e 10 voltas, retornando de quem foi a 
    melhor volta, com qual tempo e em qual volta
    list(list) -> tuple'''
    
    corredores = []
    voltas = []
    tempos_min = []
    
    for i in m:
        corredores += [list.index(m,i)+1,]
        tempos_min += [min(i),]
        
    menor_tempo = min(tempos_min)
    corredor = list.index(tempos_min,menor_tempo)+1
    
    for i in m:
        for j in i:
            if j == menor_tempo:
                melhor_volta = list.index(i,j)+1
      
    return (corredor, menor_tempo, melhor_volta)