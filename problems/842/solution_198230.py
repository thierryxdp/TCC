def pontos_por_time(lista):
    pontosportime = {'Cormengo': int(x) + int(z), 'Flamínthians': int(y) + int(w)}
    x = [] 
    y = []
    z = []
    w = []
    if lista[0][2][0] > lista[0][2][1]:
        x[0] == 3 and y[0] == 0
    if lista[0][2][0] == lista[0][2][1]:
        x[0] == 1 and y[0] == 1
    if lista[0][2][0] < lista[0][2][1]:
        x[0] == 0 and y[0] == 3
    if lista[1][2][0] < lista[1][2][1]:
        z[0] == 3 and w[0] == 0
    if lista[1][2][0] == lista[1][2][1]:
        z[0] == 1 and w[0] == 1
    if lista[0][2][0] > lista[0][2][1]:
        z[0] == 0 and w[0] == 3
    return pontosportime
        #Start your python function here