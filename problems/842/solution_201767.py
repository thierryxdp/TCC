def pontos_por_time(l):
    '''
    '''
    time1= l[0][0]
    time2= l[1][0]
    if l[0][2][0]>l[0][2][1]:
        pontos_time1j1=3
        pontos_time2j1=0
    if l[0][2][0]==l[0][2][1]:
        pontos_time1j1=1
        pontos_time2j1=1
    if l[0][2][0]<l[0][2][1]:
        pontos_time1j1=0
        pontos_time2j1=3
    if l[1][2][0]>l[1][2][1]:
        pontos_time1j2=0
        pontos_time2j2=3
    if l[1][2][0]==l[1][2][1]:
        pontos_time1j2=1
        pontos_time2j2=1
    if l[1][2][0]<l[1][2][1]:
        pontos_time1j2=3
        pontos_time2j2=0
    pontos1= pontos_time1j1 + pontos_time1j2
    pontos2= pontos_time2j1 + pontos_time2j2
    return {time1:pontos1, time2:pontos2}