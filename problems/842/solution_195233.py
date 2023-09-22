def pontos_por_time(lista):
     time = {lista[0][0]:0, lista[0][1]:0}
    for i in lista:
        if i[2][0] == i[2][1]:
            time[lista[0][0]] += 1
            time[lista[0][1]] += 1
        else:
            if i[2][0] > i[2][1]:
                time[i[0]] += 3
            elif i[2][0] < i[2][1]:
                time[i[1]] += 3
    return time