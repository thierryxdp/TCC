def pontos_por_time (lista=[[lista1],[lista2]]):
    '''
    função que recebe uma lista de dois elementos, onde cada elemento é também uma lista
    que cmpleta, tem informações do número de gols, em dois jogos de futebol entre dois 
    times, no formato: [['cormengo','flaminthians',[1,0]]
    '''
    lista1 = [time1,time2,[gols1,gols2]]
    lista2 = [time2,time1,[gols3,gols4]]
    if gols1 > gols2 and gols4 > gols3:
        return {'time1':6,'time2':0}