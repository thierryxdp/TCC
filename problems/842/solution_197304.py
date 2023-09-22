def pontos_por_time(lista):
    time1=lista[0][0]
    time2=lista[0][1]
    ida1=lista[0][2][0]
    ida2=lista[0][2][1]
    time1=lista[1][1]
    time2=lista[1][0]
    volta1=lista[1][2][1]
    volta2=lista[1][2][0]
    if ida1>ida2 and volta1>volta2:
        return {time1:6,time2:0}
    if ida1>ida2 and volta1<volta2:
        return {time1:3,time2:3}
    if ida1<ida2 and volta1<volta2:
        return {time1:0,time2:3}
    if ida1<ida2 and volta1>volta2:
        return {time1:3,time2:3}