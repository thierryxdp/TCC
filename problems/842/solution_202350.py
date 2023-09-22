def pontos_grupo(ida):
    '''Recebe uma lista de dois elementos com informaçoes do numero de gols em
    dois jogos de futebol entre dois times (ida e volta). Entrada: list->dict'''
    grupo1=0
    grupo2=0

    if ida[0][2][0]>ida[0][2][1] and ida[1][2][1]>ida[1][2][0]:
        grupo1=grupo1+6
        grupo2=grupo2+0
    elif ida[0][2][0]<ida[0][2][1] and ida[1][2][1]<ida[1][2][0]:
        grupo1=grupo1+0
        grupo2=grupo2+6
    elif ida[0][2][0]==ida[0][2][1] and ida[1][2][1]==ida[1][2][0]:
        grupo1=grupo1+2
        grupo2=grupo2+2
    elif ida[0][2][0]>ida[0][2][1] and ida[1][2][1]<ida[1][2][0]:
        grupo1=grupo1+3
        grupo2=grupo2+3
    elif ida[0][2][0]==ida[0][2][1] and ida[1][2][1]>ida[1][2][0]:
        grupo1=grupo1+4
        grupo2=grupo2+1
    elif ida[0][2][0]==ida[0][2][1] and ida[1][2][1]<ida[1][2][0]:
        grupo1=grupo1+1
        grupo2=grupo2+4
    elif ida[0][2][0]==ida[0][2][1] and ida[1][2][1]<ida[1][2][0]:
        grupo1=grupo1+1
        grupo2=grupo2+4
    time1
    time2
    valor={ida[0][0]:grupo1,ida[0][1]:time2}
    return valor