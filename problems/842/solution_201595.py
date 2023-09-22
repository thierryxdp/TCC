def pontos_por_time (lista):
    r=[]
    if ((lista[0])[2])[0] > ((lista[0])[2])[1]:
        return r + [3]
    elif ((lista[0])[2])[0] == ((lista[0])[2])[1]:
        return r + 1
    else:
        return r