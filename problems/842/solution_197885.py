def pontos_por_time(lista):
    A = 0
    B = 0
    if lista[0][2][0] > lista[0][2][1]:
        A = A + 3
    elif lista[0][2][0] < lista[0][2][1]:
        B = B + 3
    else:
        A = A + 1
        B = B + 1
    if lista[1][2][1] > lista[1][2][0]:
        A = A + 3
    elif lista[1][2][1] < lista[1][2][0]:
        B = B + 3
    else:
        B = B + 1
        A = A + 1
    if A > B:
        return {lista[0][0]: A, lista[0][1]: B}
    else:
        return {lista[0][1]: B, lista[1][0]: A}