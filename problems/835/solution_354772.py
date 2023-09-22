def melhor_volta(matriz):
    a = 100000000000
    for x in range(len(matriz)):
        for y in range(len(matriz[x-1])):
            if matriz[x-1][y-1] < a:
                a = matriz[x-1][y-1]
                b = x
                if y != 0:
                    c = y
                else: c = 10
    return (b,a,c)