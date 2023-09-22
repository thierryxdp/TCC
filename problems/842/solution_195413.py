#Start your python function here
def pontos_por_time(x):
    [a,b] = x
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
    resultado = {'Cormengo': cont_Cor, 'Flamínthians': cont_Fla}
    return resultado