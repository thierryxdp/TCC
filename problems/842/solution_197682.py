def pontos_por_time(lista):
'''
       Funação que recebe uma lista com 2 elementos com o número
       de gols em 2 jogos de futebol entre 2 times e retorna um dicionario
       com os pontos referente a cada a time
       list -> dict
    '''
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
    elif ida1>ida2 and volta1<volta2:
        return {time1:3,time2:3}
    elif ida1<ida2 and volta1<volta2:
        return {time1:0,time2:6}
    elif ida1<ida2 and volta1>volta2:
        return {time2:3,time1:3}
    elif ida1==ida2 and volta1==volta2:
        return {time1:1,time2:1}
    elif ida1==ida2 and volta1>volta2:
        return {time1:4,time2:1}
    elif ida1==ida2 and volta1<volta2:
        return {time1:1,time1:4}
    elif ida1<ida2 and volta1==volta2:
        return {time1:1,time2:4}
    elif ida1>ida2 and volta1==volta2:
        return {time1:4,time2:1}