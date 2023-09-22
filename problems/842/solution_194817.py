def ida(n1,n2):
    if n1>n2:
        return [3,0]
    elif n1==n2:
        return [1,1]
    else:
        return [0,3]
def volta(n3,n4):
    if n3>n4:
        return [0,3]
    elif n3==n4:
        return [1,1]
    else:
        return [3,0]
def pontos_por_time(lista):
    lista1 = lista[0]
    lista2 = lista[1]
    gol_ida = lista1[2]
    gol_volta = lista2[2]
    n1 = gol_ida[0]
    n2 = gol_ida[1]
    n3 = gol_volta[0]
    n4 = gol_volta[1]
    timaA = ida(n1,n2)[0] + volta(n3,n4)[0]
    timaB = ida(n1,n2)[1] + volta(n3,n4)[1]
    if timeA>=timeB:
        return {lista1[0]:timeA, lista2[0]:timeB}
    else:
        return {lista2[0]:timeB, lista1[0]:timeA}