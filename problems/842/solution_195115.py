def pontos_por_time(lista):
    """retorna um dicionario que liga o nome do time como chave e seus pontos na fase; list -> dict"""
    if lista[0][0]!=lista[1][0]:
        time_1=lista[0][0] and time_2=lista[1][0]
    else: 
        lista[0][0]==lista[1][0]
        time_1=lista[0][0] and time_2=lista[1][1]
    if lista[0][2][0]-lista[0][2][1]>0 and lista[1][2][1]-lista[1][2][0]>0:
        return {time_1:6,time_2:0}
    elif lista[0][2][0]-lista[0][2][1]>0 and lista[1][2][1]-lista[1][2][0]==0:
        return {time_1:4,time_2:1}
    elif lista[0][2][0]-lista[0][2][1]>0 and lista[1][2][1]-lista[1][2][0]<0:
        return {time_1:3,time_2:3}
    elif lista[0][2][0]-lista[0][2][1]==0 and lista[1][2][1]-lista[1][2][0]>0:
        return {time_1:4,time_2:1}
    elif lista[0][2][0]-lista[0][2][1]==0 and lista[1][2][1]-lista[1][2][0]==0:
        return {time_1:2,time_2:2}
    elif lista[0][2][0]-lista[0][2][1]==0 and lista[1][2][1]-lista[1][2][0]<0:
        return {time_1:1,time_2:4}
    elif lista[0][2][0]-lista[0][2][1]<0 and lista[1][2][1]-lista[1][2][0]>0:
        return {time_1:3,time_2:3}
    elif lista[0][2][0]-lista[0][2][1]<0 and lista[1][2][1]-lista[1][2][0]==0:
        return {time_1:1,time_2:4}
    elif lista[0][2][0]-lista[0][2][1]<0 and lista[1][2][1]-lista[1][2][0]<0:
        return {time_1:0,time_2:6}