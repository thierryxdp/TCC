def time1 (lista):
    r = (0)
    if (((lista[0])[2])[0] > ((lista[0])[2])[1]):
        r = r + (3)
    if ((lista[0])[2])[0] == ((lista[0])[2])[1]:
        r = r + (1) 
    if ((lista[1])[2])[0] < ((lista[1])[2])[1]:
        r = r + (3)
    if ((lista[1])[2])[0] == ((lista[1])[2])[1]:
        r = r + (1)
    return r

def time2 (lista):
    f = (0)
    if (((lista[0])[2])[0] < ((lista[0])[2])[1]):
        f = f + (3)
    if ((lista[0])[2])[0] == ((lista[0])[2])[1]:
        f = f + (1) 
    if ((lista[1])[2])[0] > ((lista[1])[2])[1]:
        f = f + (3)
    if ((lista[1])[2])[0] == ((lista[1])[2])[1]:
        f = f + (1)
    return f

def pontos_por_time(lista):
    return {(lista[0][0]): time2(lista), (lista[0][1]): time2(lista)}