def pontos_por_time(listajogo1,listajogo2):
    ''' sem tempo pra comentario'''
    time1= listajogo1[0]
    time2= listajogo1[1]
    pontos1=0
    pontos2=0
    times= {time1:pontos1 ,time2:pontos2}
    if listajogo1[2][0]>listajogo1[2][1]:
        pontos1= pontos1+3
    if listajogo2[2][0]>listajogo2[2][1]:
        pontos2= pontos2+3
    if listajogo1[2][0]<listajogo1[2][1]:
        pontos2= pontos2+3
    if listajogo2[2][0]<listajogo2[2][1]:
        pontos1= pontos1+3
    if listajogo1[2][0]==listajogo1[2][1]:
        pontos1=pontos1+1
        pontos2=pontos2+1
    if listajogo2[2][0]==listajogo2[2][1]:
        pontos1=pontos1+1
        pontos2=pontos2+1
        return times