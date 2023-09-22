def pontos_por_time(time1,time2):
    '''entrada:list, list; saida:list'''
    pontos = [[time1],[time2]]
    if time1>time2:
        pontos[0] = ['3']
        return pontos
    if time1<time2:
        pontos[1] = ['3']
        return pontos
    if time1==time2:
        pontos[0,1] = ['1']
        return pontos