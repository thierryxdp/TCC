def pontos_por_time(lista):

    time1 = []
    time2 = []

    saldo1 = lista[0][2][0] - lista[0][2][1]
    saldo2 = lista[1][2][0] - lista[1][2][1]

    if saldo1 == 0:
        time1.append(1)
        time2.append(1)
    if saldo1 > 0:
        time1.append(3)
    if saldo1 < 0:
        time2.append(3)

    if saldo2 == 0:
        time1.append(1)
        time2.append(1)
    if saldo2 > 0:
        time2.append(3)
    if saldo2 < 0:
        time1.append(3)

    dicionario = {lista[1][0]: sum(time1),
                  lista[0][0]: sum(time2)}
    
    return dicionario