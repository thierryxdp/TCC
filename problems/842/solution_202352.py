def pontos_por_time(ida):
    '''Recebe uma lista de dois elementos com informações do número de gols
    em dois jogos de futebol entre dois times (ida e volta).
    list -> dict'''
    time1=0
    time2=0

    if ida[0][2][0]>ida[0][2][1] and ida[1][2][1]>ida[1][2][0]:
        time1=time1+6
        time2=time2+0
    elif ida[0][2][0]<ida[0][2][1] and ida[1][2][1]<ida[1][2][0]:
        time1=time1+0
        time2=time2+6
    elif ida[0][2][0]==ida[0][2][1] and ida[1][2][1]==ida[1][2][0]:
        time1=time1+2
        time2=time2+2
    elif ida[0][2][0]>ida[0][2][1]and ida[1][2][1]<ida[1][2][0]:
        time1=time1+3
        time2=time2+3
    elif ida[0][2][0]<ida[0][2][1]and ida[1][2][1]>ida[1][2][0]:
        time1=time1+3
        time2=time2+3
    elif ida[0][2][0]==ida[0][2][1] and ida[1][2][1]>ida[1][2][0]:
        time1=time1+4
        time2=time2+1
    elif ida[0][2][0]==ida[0][2][1] and ida[1][2][1]<ida[1][2][0]:
        time1=time1+1
        time2=time2+4
    elif ida[0][2][0]<ida[0][2][1] and ida[1][2][1]==ida[1][2][0]:
        time1=time1+1
        time2=time2+4
    time1
    time2
    saldo={ida[0][0]:time1,ida[0][1]:time2}
    return saldo