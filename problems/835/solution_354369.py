def melhor_volta(matriz):
    s = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            s += [matriz[i][j],]
               t = list.index(s,min(s))
                if t<=5:
                    p = 1
                if t<=11:
                    p = 2
                if t<=17:
                    p = 3
                if t<=23:
                    p = 4
                if t<=29:
                    p = 5
                if t<=35:
                    p = 6
                if t<=41:
                    p=7
    return s