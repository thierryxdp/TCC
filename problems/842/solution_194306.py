def pontos_por_time (lista):
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
        return {lista[0][0]: 6, lista[0][1]: 0}
    if lista[0][2][0] < lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
        return {lista[0][0]: 0, lista[0][1]: 6}