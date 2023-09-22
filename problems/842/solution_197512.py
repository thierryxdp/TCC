def pontos_por_time(lista):
    '''Funcao que recebe uma lista de dois elemento e retorna um dicionario com
    numero de pontos na fase
    list->dict
    '''
    pontos1=0
    pontos2=0
    time1=lista[0][0]
    time2=lista[0][1]
    

   
    if lista[0][2][0] > lista[0][2][1]:
    	pontos1=pontos1+3
    if lista[0][2][1] > lista[0][2][0]:
    	pontos2=pontos2+3
    else:
        pontos1=pontos1+1
        pontos2=pontos2+1
    #segundo jogo
        
    if time1==lista[1][0]:
   
        if lista[1][2][0] > lista[1][2][1]:
            pontos1=pontos1+3
        if lista[1][2][1] > lista[1][2][0]:
            pontos2=pontos2+3
        else:
            pontos1=pontos1+1
            pontos2=pontos2+1
    else:
        if lista[1][2][0] > lista[1][2][1]:
            pontos2=pontos2+3
        if lista[1][2][1] > lista[1][2][0]:
            pontos1=pontos1+3
        else:
            pontos1=pontos1+1
            pontos2=pontos2+1
 
    dicio_time={time1:pontos1,time2:pontos2}
    
    return dicio_time