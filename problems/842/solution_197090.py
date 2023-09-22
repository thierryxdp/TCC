def pontos_por_time1(x):
    '''Função que dado uma lista contendo informações 
    de dois jogos, retona a quantidade de pontos dos times
    ''''
    [a,b] = x
    a[0] = nome1
    a[1] = nome2
    cont_Cor = 0
    cont_Fla = 0
    if a[2][0] == a[2][1]:
        cont_Cor += 1
        cont_Fla += 1
    elif a[2][0] > a[2][1]:
        cont_Cor += 3
    else:
        cont_Fla += 3
    if b[2][0] == b[2][1]:
        cont_Cor += 1
        cont_Fla += 1
    elif b[2][0] > b[2][1]:
        cont_Fla += 3
    else:
        cont_Cor += 3
    resultado = {nome1: cont_Fla, nome2: cont_Cor}
    return resultado