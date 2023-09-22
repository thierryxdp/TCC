def pontos_por_time(lista):
    '''Funcao que recebe uma lista com 2 listas dentro,com os numeros de gols do jogo de ida e volta
    list->dict'''
    
    
    time_1=lista[0][0]
    time_2=lista[0][1]
    
    if lista[0][2][0]>lista[0][2][1]:
        pontos_t1_j1=3
        pontos_t2_j1=0
      
    if lista[0][2][0]==lista[0][2][1]:
        pontos_t1_j1=1
        pontos_t2_j1=1
        
    if lista[0][2][0]<lista[0][2][1]:
        pontos_t1_j1=0
        pontos_t2_j1=3
        
    if lista[1][2][0]>lista[1][2][1]:
        pontos_t1_j1=0
        pontos_t2_j1=3
      
    if lista[1][2][0]==lista[1][2][1]:
        pontos_t1_j1=1
        pontos_t2_j1=1
        
    if lista[1][2][0]<lista[1][2][1]:
        pontos_t1_j1=3
        pontos_t2_j1=0
        
    pontos_t1=pontos_t1_j1+pontos_t1_j2
    pontos_t2=pontos_t2_j1+pontos_t2_j2
        
    return{time_1:pontos_t1,time_2:pontos_t2}