def pontos_por_time(lista):
    a = 0
    b = 0
    if lista[0][2][0] > lista[0][2][1]:
        a = a + 3
    if lista[0][2][0] < lista[0][2][1]:
        b = b + 3
    if lista[0][2][0] == lista[0][2][1]:
        a = a + 1
        b = b + 1
    if lista[1][2][0] > lista[1][2][1]:
        b = b + 3
    if lista[1][2][1] > lista[1][2][0]:
        a = a + 3
    if lista[1][2][1] == lista[1][2][0]:
        a = a + 1
        b = b + 1
    if a > b:
        return {lista[0][0]: a, lista[0][1]: b}