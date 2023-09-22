#Start your python function here
def pontos_por_time (lista):
    time1A = lista [0],[0]:
    time1B = lista [0],[1]:
    time2A = lista [1],[0]:
    time2B = lista [1],[1]:
    dicionario = {time1A : 0, time1B : 0}:
    gols1 = lista [0][2]
    gols2 = lista [1][2]
    if gols1 [0] == gols1[1]:
        dicionario [tima1A] +=1
        dicionario [time1B] +=1
    if gols1 [0] > gols [1]:
        decionario [time1A] +=3
        dicionario [time1B] +=0
    if gols1 [0] < gols1 [1]:
        dicionario [time1B] +=3
        dicionario [time1A] +=0
    
    if gols2 [0] ==gols2[1]:
        dicionario [time2A] +=1
        dicionario [time2B] +=1
    if gols2 [0] > gols2[1]:
        dicionario [time2A] +=3
        dicionario [time2B] +=0
    if gols2[0] < gols2[1]:
        dicionario [time2B] +=3
        dicionario [time2A] +=0
        
    return dicionario