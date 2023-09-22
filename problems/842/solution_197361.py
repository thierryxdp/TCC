def pontos_por_time(lista):
    '''Funcao que recebe uma lista de dois elemento e retorna um dicionario com
    numero de pontos na fase
    list->dict
    '''
    dicio_time={lista[0][0][0]:0,lista[0][0][1]:0}
    pontos1=0
    pontos2=0
    time1=list(dicio_time.keys()).index(lista[0][1][0])
    time2=list(dicio_time.keys()).index(lista[0][1][1])
    if lista[time1]>lista[time2]:
    	pontos1=pontos1+3
    if lista[time1]>lista[time2]:
    	pontos2=pontos2+3
    else
    	pontos1=pontos1+1
        pontos2=pontos2+1
    #segundo jogo
   
    if lista[time1]>lista[time2]:
    	pontos1=pontos1+3
    if lista[time1]>lista[time2]:
    	pontos2=pontos2+3
	else
    	pontos1=pontos1+1
        pontos2=pontos2+1
    dicio_time.update({time1:pontos1,time2:pontos2})
    return dicio_time