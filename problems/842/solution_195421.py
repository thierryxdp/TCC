#Start your python function here
def pontos_por_time(x):
    nome1 = a[0]
    nome2 = a[1]
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
    resultado = {nome1: cont_Cor, nome2: cont_Fla}
    return resultado