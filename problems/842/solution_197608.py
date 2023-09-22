def pontos_por_time(i,v):
    """Calcula os pontos dos times após dois jogos; list,list -> dict"""
    time_1 = i[0]
    time_2 = v[0]
    pontos_time_1=0
    pontos_time_2=0
    if i[2][0]>i[2][1]:
        pontos_time_1+=3
    if i[2][0]<i[2][1]:
        pontos_time_2+=3
    if v[2][1]>v[2][0]:
        pontos_time_1+=3
    if v[2][1]<v[2][0]:
        pontos_time_2+=3
    if i[2][0]==i[2][1]:
        pontos_time_1+=1
        pontos_time_2+=1

        
    return {time_1:pontos_time_1, time_2:pontos_time_2}#Start your python function here