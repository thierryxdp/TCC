def pontos_por_time(x):
    '''Função que dado uma lista contendo informações 
    de dois jogos, retona a quantidade de pontos dos times
    ''''
    [a,b] = x
    nome1 = a[0]
    nome2 = a[1]
    contt1 = 0
    contt2 = 0
    if a[2][0] == a[2][1]:
        contt1 += 1
        contt2 += 1
    elif a[2][0] > a[2][1] or a[2][1] > a[2][0]:
        if a[2][0] > a[2][1]:
            contt1 += 3
        else:
            contt2 += 3
    if b[2][0] == b[2][1]:
        contt1 += 1
        contt2 += 1
    elif b[2][0] > b[2][1] or b[2][1] > b[2][0]:
        if b[2][0] > b[2][1]:
            contt2 += 3
        else:
            contt1 += 3
    resultado = {nome1: contt1, nome2: contt2}
    return resultado#Start your python function here