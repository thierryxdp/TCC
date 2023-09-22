def pontos_por_time (lista):
    r = (0)
    if (((lista[0])[2])[0] > ((lista[0])[2])[1]):
         r + (3)
    if ((lista[0])[2])[0] == ((lista[0])[2])[1]:
        return r + (1) 
    if ((lista[1])[2])[0] < ((lista[1])[2])[1]:
         r + (3)
    if ((lista[1])[2])[0] == ((lista[1])[2])[1]:
        return r + (1)
    return r