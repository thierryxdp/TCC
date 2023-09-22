def pontos_por_time(time1,time2,placar1,placar2):
    """função que retorna um dicionario com o nome do time e sua pontuação
    lista -> dicionario"""
    placar1 = [x,y] 
    placar2 = [x,y]  
    if [[time1,time2,[ x>y ]], [time2,time1,[x<y]]]:
        return {time1:6 , time2:0}