def melhor_volta(m):
    '''recebe como entrada uma matriz de tamanho 6x10, com os segundos dos corredores em cada volta. Calcula e retorna uma tupla de queml foi a melhor volta, com qual tempo e em que volta isso ocorreu'''
    '''list(list) -> tuple'''
    volta = []
    tempos_minutos = []
    
    for listas in m:
        tempos_minutos += [min(listas),]
        
    menor_t = min(tempos_minutos)
    corredor = list.index(tempos_minutos,menor_t)+1
    
    for listas in m:
        for j in listas:
            if j == menor_t:
                melhor_volta = list.index(listas,j)+1
      
    return (corredor, menor_t, melhor_volta)