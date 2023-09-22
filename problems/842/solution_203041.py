def pontos_por_time(fase):
    '''A função retorna o total de pontos de dois times, dadas duas
    listas onde uma contém as informações do jogo de ida e a outra,
    as informações sobre o jogo da volta. As informações devem ser
    introduzidas no seguinte formato:
    [[time1,time2,gols_ida_time1,gols_ida_time2],[time2,time1,
    gols_volta_time2,gols_volta_time1]].
    lista,lista -> dicionário'''
    #fase=[[time1,time2,[gols_ida1,gols_ida2]],[time2,time1,[gols_volta2,gols_volta1]]]
    p1=0
    p2=0
    if fase[0][2][0]>fase[0][2][1]:
    	p1=p1+3
    elif fase[0][2][0]<fase[0][2][1]:
    	p2=p1+3
    else:
    	p1=p1+1
    	p2=p2+1
    if fase[1][2][0]>fase[1][2][1]:
    	p2=p2+3
    elif fase[1][2][0]<fase[1][2][1]:
    	p1=p1+3
    else:
    	p1=p1+1
    	p2=p2+1
    return {fase[0][0]:p1,fase[0][1]:p2}