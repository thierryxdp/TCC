def pontos_por_time(listajogo):
    ''' sem tempo pra comentario'''
    time1= listajogo[0][0]
    time2= listajogo[0][1]
    pontos1=0
    pontos2=0
    times= {time1:pontos1 ,time2:pontos2}
    if listajogo[0][2][0]>listajogo[0][2][1]:
        pontos1= pontos1+3
    if listajogo[1][2][0]>listajogo[1][2][1]:
        pontos2= pontos2+3
    if listajogo[0][2][0]<listajogo[0][2][1]:
        pontos2= pontos2+3
    if listajogo[1][2][0]<listajogo[1][2][1]:
        pontos1= pontos1+3
    if listajogo[0][2][0]==listajogo[0][2][1]:
        pontos1=pontos1+1
        pontos2=pontos2+1
    if listajogo[1][2][0]==listajogo[1][2][1]:
        pontos1=pontos1+1
        pontos2=pontos2+1
        return times