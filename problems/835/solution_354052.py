def melhor_volta(x):
    """
    list -> tuple
    """
    temp = volta = venc = 1000
    for v in range(0, len(x)):
        for t in range(0, len(x[v])):
            if min(x[v][t], temp) == x[v][t]:
                temp = min(x[v][t], temp)
                venc = v + 1
                volta = t + 1