def pontos(a):
    if (a[0][2][0]) > (a[0][2][1]):
        return 3
    if (a[0][2][0]) == (a[0][2][1]):
        return 1
    else:
        return 0

def pontos1(b):
    if (b[1][2][1]) > (b[1][2][0]):
        return 3
    if (b[1][2][1]) == (b[1][2][0]):
        return 1
    else:
        return 0