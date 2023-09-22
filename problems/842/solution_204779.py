def pontos(a):
    if (a[0][2][0]) > (a[0][2][1]):
        return 3
    if (a[0][2][0]) == (a[0][2][1]):
        return 1
    else:
        return 0

def pontos1(b):
    if (b[1][2][0]) > (b[1][2][1]):
        return 3
    if (b[0][2][0]) == (b[0][2][1]):
        return 1
    else:
        return 0


def pontos_por_time(a):
    if pontos(a) + pontos1(a) == 0:
        return {(a[0][0]): pontos(a)+ pontos1(a) , (a[0][1]): 6}
    if pontos(a) + pontos1(a) == 1:
        return {(a[0][0]): pontos(a)+ pontos1(a) , (a[0][1]): 4}
    if pontos(a) + pontos1(a) == 2:
        return {(a[0][0]): pontos(a)+ pontos1(a), (a[0][1]): 2}
    if pontos(a) + pontos1(a) == 3:
        return {(a[0][0]): pontos(a)+ pontos1(a),(a[0][1]): 3}
    if pontos(a) + pontos1(a) == 4:
        return {(a[0][0]): pontos(a)+ pontos1(a), (a[0][1]): 1}
    if pontos(a) + pontos1(a) == 6:
        return {(a[0][0]): pontos(a) + pontos1(a), (a[0][1]): 0}