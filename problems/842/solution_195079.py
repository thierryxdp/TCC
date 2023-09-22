def pontos_por_time(lista):
    """retorna um dicionario que liga o nome do time como chave e seus pontos na fase; list -> dict"""
    time_2=lista[0][0]
    time_1=lista[1][0]
    if lista[0][2][0]-lista[0][2][1]>0 and lista[1][2][1]-lista[1][2][0]>0:
        return {"Cormengo":6,"Flamínthians":0}
    elif lista[0][2][0]-lista[0][2][1]>0 and lista[1][2][1]-lista[1][2][0]==0:
        return {"Cormengo":4,"Flamínthians":1}
    elif lista[0][2][0]-lista[0][2][1]>0 and lista[1][2][1]-lista[1][2][0]<0:
        return {"Cormengo":3,"Flamínthians":3}
    elif lista[0][2][0]-lista[0][2][1]==0 and lista[1][2][1]-lista[1][2][0]>0:
        return {"Cormengo":4,"Flamínthians":1}
    elif lista[0][2][0]-lista[0][2][1]==0 and lista[1][2][1]-lista[1][2][0]==0:
        return {"Cormengo":2,"Flamínthians":2}
    elif lista[0][2][0]-lista[0][2][1]==0 and lista[1][2][1]-lista[1][2][0]<0:
        return {"Cormengo":1,"Flamínthians":4}
    elif lista[0][2][0]-lista[0][2][1]<0 and lista[1][2][1]-lista[1][2][0]>0:
        return {"Cormengo":3,"Flamínthians":3}
    elif lista[0][2][0]-lista[0][2][1]<0 and lista[1][2][1]-lista[1][2][0]==0:
        return {"Cormengo":1,"Flamínthians":4}
    elif lista[0][2][0]-lista[0][2][1]<0 and lista[1][2][1]-lista[1][2][0]<0:
        return {"Cormengo":0,"Flamínthians":6}